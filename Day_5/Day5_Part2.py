import re
import Maps

seeds = [
    2149186375,
    163827995,
    1217693442,
    67424215,
    365381741,
    74637275,
    1627905362,
    77016740,
    22956580,
    60539394,
    586585112,
    391263016,
    2740196667,
    355728559,
    2326609724,
    132259842,
    2479354214,
    184627854,
    3683286274,
    337630529]
seeds_source_ranges = []
seeds_ranges = []
soils_ranges = []
fertilizers_ranges = []
waters_ranges = []
lights_ranges = []
temperatures_ranges = []
humidities_ranges = []
locations_ranges = []

def overlap (r1_start, r1_stop, r2_start, r2_stop):
    return range(max(r1_start, r2_start), min(r1_stop, r2_stop)) or None

def map_to_range(source_ranges, map, map_lines):
    second_ranges = []
    for s in source_ranges:
        n = 0
        for x in map:
            second = int(map_lines[n][0])
            first = int(map_lines[n][1])
            range_lenght = int(map_lines[n][2])
            first_range = (first, first + range_lenght)
            n += 1
            overlap_source = overlap(*s, *first_range)
            if overlap_source != None:
                second_range = (second, second + range_lenght)
                diff_ranges = ((overlap_source.start - first_range[0] + second_range[0]),
                               (overlap_source.stop - first_range[1] + second_range[1]))
                second_ranges.append(diff_ranges)
    return second_ranges


count = 0
for y in range(0, len(seeds), 2):
    start = seeds[y]
    stop = start + seeds[y + 1]
    seeds_source_ranges.append((start, stop))


soils_ranges = map_to_range(seeds_source_ranges, Maps.SeedToSoil_, Maps.SeedToSoil_lines)

fertilizers_ranges = map_to_range(soils_ranges, Maps.SoilToFertilizer_, Maps.SoilToFertilizer_lines)
waters_ranges = map_to_range(fertilizers_ranges, Maps.FertilizerToWater_, Maps.FertilizerToWater_lines)
lights_ranges = map_to_range(waters_ranges, Maps.WaterToLight_, Maps.WaterToLight_lines)
temperatures_ranges = map_to_range(lights_ranges, Maps.LightToTemperature_, Maps.LightToTemperature_lines)
humidities_ranges = map_to_range(temperatures_ranges, Maps.TemperatureToHumidity_, Maps.TemperatureToHumidity_lines)
locations_ranges = map_to_range(humidities_ranges, Maps.HumidityToLocation_, Maps.HumidityToLocation_lines)

min = min(locations_ranges)[0]
print(min)


