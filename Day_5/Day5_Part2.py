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

count = 0
for y in range(0, len(seeds), 2):
    start = seeds[y]
    stop = start + seeds[y + 1]
    seeds_source_ranges.append((start, stop))

#z tego zrobic funkcje:
for s in seeds_source_ranges:
    n = 0
    for x in Maps.SeedToSoil_:
        soil = int(Maps.SeedToSoil_lines[n][0])
        seed = int(Maps.SeedToSoil_lines[n][1])
        range_lenght = int(Maps.SeedToSoil_lines[n][2])
        seed_range = (seed, seed + range_lenght)
        n += 1
        overlap_source = overlap(*s, *seed_range)
        if overlap_source != None:
            seeds_ranges.append(overlap_source)
            soil_range = (soil, soil + range_lenght)
            diff_ranges = ((overlap_source[0] - seed_range[0] + soil_range[0]), (overlap_source[1]) - seed_range[1] + soil_range[1])
            soils_ranges.append(diff_ranges)

# i wywolywac tu:

for s in soils_ranges:
    n = 0
    for x in Maps.SoilToFertilizer_:
        fertilizer = int(Maps.SoilToFertilizer_lines[n][0])
        soil = int(Maps.SoilToFertilizer_lines[n][1])
        range_lenght = int(Maps.SoilToFertilizer_lines[n][2])
        soil_range = (soil, soil + range_lenght)
        fertilizer_range = (fertilizer, fertilizer + range_lenght)
        diff_ranges = ((s[0] - soil_range[0] + fertilizer_range[0]), (s[1]) - soil_range[1] + fertilizer_range[1])
        fertilizers_ranges.append(diff_ranges)



for f in fertilizers_ranges:
    n = 0
    for x in Maps.FertilizerToWater_:
        water = int(Maps.FertilizerToWater_lines[n][0])
        fertilizer = int(Maps.FertilizerToWater_lines[n][1])
        range_lenght = int(Maps.FertilizerToWater_lines[n][2])
        fertilizer_range = (fertilizer, fertilizer + range_lenght)
        water_range = (water, water + range_lenght)
        diff_ranges = ((f[0] - fertilizer_range[0] + water_range[0]), (f[1]) - fertilizer_range[1] + water_range[1])
        waters_ranges.append(diff_ranges)

for w in waters_ranges:
    n = 0
    for x in Maps.WaterToLight_:
        light = int(Maps.WaterToLight_lines[n][0])
        water = int(Maps.FertilizerToWater_lines[n][1])
        range_lenght = int(Maps.FertilizerToWater_lines[n][2])
        light_range = (light, light + range_lenght)
        water_range = (water, water + range_lenght)
        diff_ranges = ((w[0] - water_range[0] + light_range[0]), (w[1]) - water_range[1] + light_range[1])
        lights_ranges.append(diff_ranges)

for l in lights_ranges:
    n = 0
    for x in Maps.LightToTemperature_:
        temperature = int(Maps.LightToTemperature_lines[n][0])
        light = int(Maps.LightToTemperature_lines[n][1])
        range_lenght = int(Maps.LightToTemperature_lines[n][2])
        temperature_range = (temperature, temperature + range_lenght)
        light_range = (light, light + range_lenght)
        diff_ranges = ((l[0] - light_range[0] + temperature_range[0]), (l[1]) - light_range[1] + temperature_range[1])
        temperatures_ranges.append(diff_ranges)

for t in temperatures_ranges:
    n = 0
    for x in Maps.TemperatureToHumidity_:
        humidity = int(Maps.TemperatureToHumidity_lines[n][0])
        temperature = int(Maps.TemperatureToHumidity_lines[n][1])
        range_lenght = int(Maps.TemperatureToHumidity_lines[n][2])
        temperature_range = (temperature, temperature + range_lenght)
        humidity_range = (humidity, humidity + range_lenght)
        diff_ranges = ((t[0] - temperature_range[0] + humidity_range[0]), (t[1]) - temperature_range[1] + humidity_range[1])
        humidities_ranges.append(diff_ranges)

for h in humidities_ranges:
    n = 0
    for x in Maps.HumidityToLocation_:
        location = int(Maps.HumidityToLocation_lines[n][0])
        humidity = int(Maps.HumidityToLocation_lines[n][1])
        range_lenght = int(Maps.HumidityToLocation_lines[n][2])
        location_range = (location, location + range_lenght)
        humidity_range = (humidity, humidity + range_lenght)
        diff_ranges = ((h[0] - humidity_range[0] + location_range[0]), (h[1]) - humidity_range[1] + location_range[1])
        locations_ranges.append(diff_ranges)

location_min = locations_ranges[0][0]
for loc in locations_ranges:
    min = loc[0]
    if min < location_min:
        location_min = min

print(location_min)