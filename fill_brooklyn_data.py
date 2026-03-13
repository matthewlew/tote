import json
import os

data = {
    'williamsburg': [
        {"brand": "Coffee Shop", "name": "Devocion", "address": "69 Grand St, Brooklyn, NY 11249"},
        {"brand": "Restaurant", "name": "Lilia", "address": "567 Union Ave, Brooklyn, NY 11211"}
    ],
    'park_slope': [
        {"brand": "Bookstore", "name": "Community Bookstore", "address": "143 7th Ave, Brooklyn, NY 11215"},
        {"brand": "Restaurant", "name": "Al Di La Trattoria", "address": "248 5th Ave, Brooklyn, NY 11215"}
    ],
    'bed_stuy': [
        {"brand": "Coffee Shop", "name": "Daily Press", "address": "505 Franklin Ave, Brooklyn, NY 11238"},
        {"brand": "Restaurant", "name": "Peaches HotHouse", "address": "415 Tompkins Ave, Brooklyn, NY 11216"}
    ],
    'greenpoint': [
        {"brand": "Bakery", "name": "Peter Pan Donut & Pastry Shop", "address": "727 Manhattan Ave, Brooklyn, NY 11222"},
        {"brand": "Restaurant", "name": "Paulie Gee's", "address": "60 Greenpoint Ave, Brooklyn, NY 11222"}
    ],
    'bushwick': [
        {"brand": "Coffee Shop", "name": "Sey Coffee", "address": "18 Grattan St, Brooklyn, NY 11206"},
        {"brand": "Restaurant", "name": "Roberta's", "address": "261 Moore St, Brooklyn, NY 11206"}
    ],
    'crown_heights': [
        {"brand": "Bar", "name": "Super Power", "address": "722 Nostrand Ave, Brooklyn, NY 11216"},
        {"brand": "Restaurant", "name": "Chavela's", "address": "736 Franklin Ave, Brooklyn, NY 11238"}
    ],
    'dumbo': [
        {"brand": "Bookstore", "name": "Powerhouse Arena", "address": "28 Adams St, Brooklyn, NY 11201"},
        {"brand": "Restaurant", "name": "Juliana's", "address": "19 Old Fulton St, Brooklyn, NY 11201"}
    ],
    'fort_greene': [
        {"brand": "Restaurant", "name": "Miss Ada", "address": "184 DeKalb Ave, Brooklyn, NY 11205"},
        {"brand": "Park", "name": "Fort Greene Park", "address": "DeKalb Ave & Washington Park, Brooklyn, NY 11205"}
    ],
    'cobble_hill': [
        {"brand": "Restaurant", "name": "La Vara", "address": "268 Clinton St, Brooklyn, NY 11201"},
        {"brand": "Bookstore", "name": "Books Are Magic", "address": "225 Smith St, Brooklyn, NY 11231"}
    ],
    'brooklyn_heights': [
        {"brand": "Park", "name": "Brooklyn Heights Promenade", "address": "Montague St & Pierrepont Pl, Brooklyn, NY 11201"},
        {"brand": "Restaurant", "name": "Noodle Pudding", "address": "38 Henry St, Brooklyn, NY 11201"}
    ],
    'carroll_gardens': [
        {"brand": "Restaurant", "name": "Frankies 457 Spuntino", "address": "457 Court St, Brooklyn, NY 11231"},
        {"brand": "Bakery", "name": "Court Street Grocers", "address": "485 Court St, Brooklyn, NY 11231"}
    ],
    'clinton_hill': [
        {"brand": "Restaurant", "name": "Aita", "address": "132 Greene Ave, Brooklyn, NY 11238"},
        {"brand": "Coffee Shop", "name": "Clementine Bakery", "address": "395 Classon Ave, Brooklyn, NY 11238"}
    ],
    'gowanus': [
        {"brand": "Brewery", "name": "Threes Brewing", "address": "333 Douglass St, Brooklyn, NY 11217"},
        {"brand": "Restaurant", "name": "Claro", "address": "284 Third Ave, Brooklyn, NY 11215"}
    ],
    'red_hook': [
        {"brand": "Restaurant", "name": "Hometown Bar-B-Que", "address": "454 Van Brunt St, Brooklyn, NY 11231"},
        {"brand": "Bar", "name": "Sunny's Bar", "address": "253 Conover St, Brooklyn, NY 11231"}
    ],
    'boerum_hill': [
        {"brand": "Restaurant", "name": "Rucola", "address": "190 Dean St, Brooklyn, NY 11217"},
        {"brand": "Restaurant", "name": "French Louie", "address": "320 Atlantic Ave, Brooklyn, NY 11201"}
    ],
    'ditmas_park': [
        {"brand": "Restaurant", "name": "The Farm on Adderley", "address": "1108 Cortelyou Rd, Brooklyn, NY 11218"},
        {"brand": "Bar", "name": "Sycamore Bar + Flower Shop", "address": "1118 Cortelyou Rd, Brooklyn, NY 11218"}
    ],
    'kensington': [
        {"brand": "Restaurant", "name": "To B Thai", "address": "426 Church Ave, Brooklyn, NY 11218"},
        {"brand": "Coffee Shop", "name": "Der Pioneer", "address": "737 Church Ave, Brooklyn, NY 11218"}
    ],
    'windsor_terrace': [
        {"brand": "Restaurant", "name": "The Double Windsor", "address": "210 Prospect Park West, Brooklyn, NY 11215"},
        {"brand": "Cafe", "name": "Krupa Grocery", "address": "231 Prospect Park West, Brooklyn, NY 11215"}
    ],
    'bay_ridge': [
        {"brand": "Restaurant", "name": "Tanoreen", "address": "7523 3rd Ave, Brooklyn, NY 11209"},
        {"brand": "Bakery", "name": "Leske's Bakery", "address": "7612 5th Ave, Brooklyn, NY 11209"}
    ],
    'sunset_park': [
        {"brand": "Restaurant", "name": "Tacos El Bronco", "address": "4324 4th Ave, Brooklyn, NY 11232"},
        {"brand": "Park", "name": "Sunset Park", "address": "41st St & 44th St, Brooklyn, NY 11232"}
    ]
}

for key, places in data.items():
    filepath = f"data/{key}.json"
    if os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({"places": places}, f, indent=2)
            print(f"Updated {filepath}")
