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
soils = []
fertilizers = []
water = []
lights = []
temperatures = []
humidities = []
locations = []

for s in seeds:
    n = 0
    for x in Maps.SeedToSoil_:
        soil = int(Maps.SeedToSoil_lines[n][0])
        seed = int(Maps.SeedToSoil_lines[n][1])
        range_lenght = int(Maps.SeedToSoil_lines[n][2])
        n += 1
        if (s > seed) & (s < ( s + range_lenght)) : #sprawdzam czy seed mieści się w zakresie i wyliczam soil
            d = s - seed
            soil_sought = soil + d
            soils.append(soil_sought)
            print(soil_sought)