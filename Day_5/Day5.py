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
SeedToSoil = []
SeedToSoil_line =[]
n = 0
SeedToSoil = Maps.SeedToSoil.split('\n')
for line in SeedToSoil:
    SeedToSoil_line = line
    print(line)
    #SeedToSoil.append(re.split("\s", Maps.SeedToSoil))

#def MapToList(map):

