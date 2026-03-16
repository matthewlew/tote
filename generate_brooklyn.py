import json
import os

neighborhoods = {
    'williamsburg': {'name': 'Williamsburg', 'lat': 40.7128, 'lng': -73.9560},
    'park_slope': {'name': 'Park Slope', 'lat': 40.6720, 'lng': -73.9778},
    'bed_stuy': {'name': 'Bedford-Stuyvesant', 'lat': 40.6872, 'lng': -73.9418},
    'greenpoint': {'name': 'Greenpoint', 'lat': 40.7302, 'lng': -73.9540},
    'bushwick': {'name': 'Bushwick', 'lat': 40.6958, 'lng': -73.9171},
    'crown_heights': {'name': 'Crown Heights', 'lat': 40.6681, 'lng': -73.9448},
    'dumbo': {'name': 'DUMBO', 'lat': 40.7033, 'lng': -73.9881},
    'fort_greene': {'name': 'Fort Greene', 'lat': 40.6861, 'lng': -73.9754},
    'cobble_hill': {'name': 'Cobble Hill', 'lat': 40.6875, 'lng': -73.9958},
    'brooklyn_heights': {'name': 'Brooklyn Heights', 'lat': 40.6950, 'lng': -73.9936},
    'carroll_gardens': {'name': 'Carroll Gardens', 'lat': 40.6805, 'lng': -73.9981},
    'clinton_hill': {'name': 'Clinton Hill', 'lat': 40.6896, 'lng': -73.9660},
    'gowanus': {'name': 'Gowanus', 'lat': 40.6731, 'lng': -73.9902},
    'red_hook': {'name': 'Red Hook', 'lat': 40.6734, 'lng': -74.0093},
    'boerum_hill': {'name': 'Boerum Hill', 'lat': 40.6845, 'lng': -73.9856},
    'ditmas_park': {'name': 'Ditmas Park', 'lat': 40.6409, 'lng': -73.9626},
    'kensington': {'name': 'Kensington', 'lat': 40.6385, 'lng': -73.9748},
    'windsor_terrace': {'name': 'Windsor Terrace', 'lat': 40.6539, 'lng': -73.9758},
    'bay_ridge': {'name': 'Bay Ridge', 'lat': 40.6262, 'lng': -74.0320},
    'sunset_park': {'name': 'Sunset Park', 'lat': 40.6455, 'lng': -74.0124},
}

for key, data in neighborhoods.items():
    filepath = f"data/{key}.json"
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({"places": []}, f, indent=2)

print("Generated JSON files.")
