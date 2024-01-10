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
waters = []
lights = []
temperatures = []
humidities = []
locations = []

for s in seeds:
    in_range = False
    n = 0
    for x in Maps.SeedToSoil_:
        soil = int(Maps.SeedToSoil_lines[n][0])
        seed = int(Maps.SeedToSoil_lines[n][1])
        range_lenght = int(Maps.SeedToSoil_lines[n][2])
        n += 1
        if (s > seed) & (s < ( seed + range_lenght)) : #sprawdzam czy seed mieści się w zakresie i wyliczam soil
            d = s - seed
            soil_sought = soil + d
            soils.append(soil_sought)
            in_range = True
    if in_range == False:
        soils.append(s)

for o in soils:
    in_range = False
    n = 0
    for x in Maps.SoilToFertilizer_:
        fertilizer = int(Maps.SoilToFertilizer_lines[n][0])
        soil = int(Maps.SoilToFertilizer_lines[n][1])
        range_lenght = int(Maps.SoilToFertilizer_lines[n][2])
        n += 1
        if (o > soil) & (o < (soil + range_lenght)):
            d = o - soil
            fertilizer_sought = fertilizer + d
            fertilizers.append(fertilizer_sought)
            in_range = True
    if in_range == False:
        fertilizers.append(o)

for f in fertilizers:
    in_range = False
    n = 0
    for x in Maps.FertilizerToWater_:
        water = int(Maps.FertilizerToWater_lines[n][0])
        fertilizer = int(Maps.FertilizerToWater_lines[n][1])
        range_lenght = int(Maps.FertilizerToWater_lines[n][2])
        n += 1
        if (f > fertilizer) & (f < (fertilizer + range_lenght)):
            d = f - fertilizer
            water_sought = water + d
            waters.append(water_sought)
            in_range = True
    if in_range == False:
        water.append(f)

for w in waters:

    in_range = False
    n = 0
    for x in Maps.WaterToLight_:
        light = int(Maps.WaterToLight_lines[n][0])
        water = int(Maps.WaterToLight_lines[n][1])
        range_lenght = int(Maps.WaterToLight_lines[n][2])
        n += 1
        if (w > water) & (w < (water + range_lenght)):
            d = w - water
            light_sought = light + d
            lights.append(light_sought)
            in_range = True
    if in_range == False:
        lights.append(w)

for l in lights:
    in_range = False
    n = 0
    for x in Maps.LightToTemperature_:
        temperature = int(Maps.LightToTemperature_lines[n][0])
        light = int(Maps.LightToTemperature_lines[n][1])
        range_lenght = int(Maps.LightToTemperature_lines[n][2])
        n += 1
        if (l > light) & (l < (light + range_lenght)):
            d = l - light
            temperature_sought = temperature + d
            temperatures.append(temperature_sought)
            in_range = True
    if in_range == False:
        temperatures.append(l)

for t in temperatures:
    in_range = False
    n = 0
    for x in Maps.TemperatureToHumidity_:
        humidity = int(Maps.TemperatureToHumidity_lines[n][0])
        temperature = int(Maps.TemperatureToHumidity_lines[n][1])
        range_lenght = int(Maps.TemperatureToHumidity_lines[n][2])
        n += 1
        if (t > temperature) & (t < (temperature + range_lenght)):
            d = t - temperature
            humidity_sought = humidity + d
            humidities.append(humidity_sought)
            in_range = True
    if in_range == False:
        humidities.append(t)

for h in humidities:
    in_range = False
    n = 0
    for x in Maps.HumidityToLocation_:
        location = int(Maps.HumidityToLocation_lines[n][0])
        humidity = int(Maps.HumidityToLocation_lines[n][1])
        range_lenght = int(Maps.HumidityToLocation_lines[n][2])
        n += 1
        if (h > humidity) & (h < (humidity + range_lenght)):
            d = h - humidity
            location_sought = location + d
            locations.append(location_sought)
            in_range = True
    if in_range == False:
        locations.append(h)

print(min(locations))
