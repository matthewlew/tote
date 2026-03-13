import json
import os

data = {
    'williamsburg': [
        {"brand": "Coffee Shop", "name": "Devocion", "links": [{"u": "https://www.devocion.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Lilia", "links": [{"u": "https://www.lilianewyork.com/", "r": "Website"}]}
    ],
    'park_slope': [
        {"brand": "Bookstore", "name": "Community Bookstore", "links": [{"u": "https://www.communitybookstore.net/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Al Di La Trattoria", "links": [{"u": "https://aldilatrattoria.com/", "r": "Website"}]}
    ],
    'bed_stuy': [
        {"brand": "Coffee Shop", "name": "Daily Press", "links": [{"u": "https://www.dailypresscoffee.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Peaches HotHouse", "links": [{"u": "https://www.bcrestaurantgroup.com/peaches-hothouse", "r": "Website"}]}
    ],
    'greenpoint': [
        {"brand": "Bakery", "name": "Peter Pan Donut & Pastry Shop", "links": [{"u": "http://peterpandonuts.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Paulie Gee's", "links": [{"u": "https://pauliegee.com/", "r": "Website"}]}
    ],
    'bushwick': [
        {"brand": "Coffee Shop", "name": "Sey Coffee", "links": [{"u": "https://www.seycoffee.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Roberta's", "links": [{"u": "https://www.robertaspizza.com/", "r": "Website"}]}
    ],
    'crown_heights': [
        {"brand": "Bar", "name": "Super Power", "links": [{"u": "https://www.superpowerbrooklyn.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Chavela's", "links": [{"u": "https://chavelasnyc.com/", "r": "Website"}]}
    ],
    'dumbo': [
        {"brand": "Bookstore", "name": "Powerhouse Arena", "links": [{"u": "https://www.powerhousearena.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Juliana's", "links": [{"u": "https://julianaspizza.com/", "r": "Website"}]}
    ],
    'fort_greene': [
        {"brand": "Restaurant", "name": "Miss Ada", "links": [{"u": "https://www.missadanyc.com/", "r": "Website"}]},
        {"brand": "Park", "name": "Fort Greene Park", "links": [{"u": "https://www.fortgreenepark.org/", "r": "Website"}]}
    ],
    'cobble_hill': [
        {"brand": "Restaurant", "name": "La Vara", "links": [{"u": "https://www.lavarany.com/", "r": "Website"}]},
        {"brand": "Bookstore", "name": "Books Are Magic", "links": [{"u": "https://www.booksaremagic.net/", "r": "Website"}]}
    ],
    'brooklyn_heights': [
        {"brand": "Park", "name": "Brooklyn Heights Promenade", "links": [{"u": "https://www.nycgovparks.org/parks/brooklyn-heights-promenade", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Noodle Pudding", "links": [{"u": "https://goo.gl/maps/1", "r": "Maps"}]}
    ],
    'carroll_gardens': [
        {"brand": "Restaurant", "name": "Frankies 457 Spuntino", "links": [{"u": "https://frankies457.com/", "r": "Website"}]},
        {"brand": "Bakery", "name": "Court Street Grocers", "links": [{"u": "https://www.courtstreetgrocers.com/", "r": "Website"}]}
    ],
    'clinton_hill': [
        {"brand": "Restaurant", "name": "Aita", "links": [{"u": "https://aitarestaurant.com/", "r": "Website"}]},
        {"brand": "Coffee Shop", "name": "Clementine Bakery", "links": [{"u": "https://clementinebakery.com/", "r": "Website"}]}
    ],
    'gowanus': [
        {"brand": "Brewery", "name": "Threes Brewing", "links": [{"u": "https://threesbrewing.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "Claro", "links": [{"u": "https://www.clarobk.com/", "r": "Website"}]}
    ],
    'red_hook': [
        {"brand": "Restaurant", "name": "Hometown Bar-B-Que", "links": [{"u": "https://hometownbbq.com/", "r": "Website"}]},
        {"brand": "Bar", "name": "Sunny's Bar", "links": [{"u": "https://www.sunnysredhook.com/", "r": "Website"}]}
    ],
    'boerum_hill': [
        {"brand": "Restaurant", "name": "Rucola", "links": [{"u": "https://rucolabrooklyn.com/", "r": "Website"}]},
        {"brand": "Restaurant", "name": "French Louie", "links": [{"u": "https://frenchlouienyc.com/", "r": "Website"}]}
    ],
    'ditmas_park': [
        {"brand": "Restaurant", "name": "The Farm on Adderley", "links": [{"u": "https://www.thefarmonadderley.com/", "r": "Website"}]},
        {"brand": "Bar", "name": "Sycamore Bar + Flower Shop", "links": [{"u": "https://sycamorebrooklyn.com/", "r": "Website"}]}
    ],
    'kensington': [
        {"brand": "Restaurant", "name": "To B Thai", "links": [{"u": "https://tobthai.com/", "r": "Website"}]},
        {"brand": "Coffee Shop", "name": "Der Pioneer", "links": [{"u": "https://derpioneer.com/", "r": "Website"}]}
    ],
    'windsor_terrace': [
        {"brand": "Restaurant", "name": "The Double Windsor", "links": [{"u": "https://thedoublewindsor.com/", "r": "Website"}]},
        {"brand": "Cafe", "name": "Krupa Grocery", "links": [{"u": "https://krupagrocery.com/", "r": "Website"}]}
    ],
    'bay_ridge': [
        {"brand": "Restaurant", "name": "Tanoreen", "links": [{"u": "https://tanoreen.com/", "r": "Website"}]},
        {"brand": "Bakery", "name": "Leske's Bakery", "links": [{"u": "https://leskesbakery.com/", "r": "Website"}]}
    ],
    'sunset_park': [
        {"brand": "Restaurant", "name": "Tacos El Bronco", "links": [{"u": "https://tacoselbronco.com/", "r": "Website"}]},
        {"brand": "Park", "name": "Sunset Park", "links": [{"u": "https://www.nycgovparks.org/parks/sunset-park", "r": "Website"}]}
    ]
}

for key, places in data.items():
    filepath = f"data/{key}.json"
    if os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({"places": places}, f, indent=2)
            print(f"Updated {filepath}")
