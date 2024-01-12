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
seeds_ranges = []
soils = []
soils_ranges = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []

def overlap (r1_start, r1_stop, r2_start, r2_stop):
    return range(max(r1_start, r2_start), min(r1_stop, r2_stop)) or None

count = 0
for y in range(0, len(seeds), 2):
    start = seeds[y]
    stop = start + seeds[y + 1]
    seeds_ranges.append((start, stop))

for s in seeds_ranges:
    #in_range = False
    n = 0
    seed_ranges = []
    for x in Maps.SeedToSoil_:
        soil = int(Maps.SeedToSoil_lines[n][0])
        seed = int(Maps.SeedToSoil_lines[n][1])
        range_lenght = int(Maps.SeedToSoil_lines[n][2])
        seed_range = (seed, seed + range_lenght)
        n += 1
        in_range = overlap(*s, *seed_range)
# tu jest coś nie halo, zapisuje takie same wyniki wiele razy:
        if in_range == None:
            soils_ranges.append(s)
        else:
            soils_ranges.append(in_range)



print(min(locations))
