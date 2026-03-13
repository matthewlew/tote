import json
import os
import requests
import time

def fetch_places(lat, lon, radius=1000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"~"cafe|restaurant|bar"](around:{radius},{lat},{lon});
      node["shop"](around:{radius},{lat},{lon});
    );
    out center 50;
    """
    for attempt in range(3):
        try:
            response = requests.get(overpass_url, params={'data': overpass_query})
            response.raise_for_status()
            return response.json().get('elements', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data (attempt {attempt+1}): {e}")
            time.sleep(10)
    return []

def extract_address(tags):
    parts = []
    if 'addr:housenumber' in tags and 'addr:street' in tags:
        parts.append(f"{tags['addr:housenumber']} {tags['addr:street']}")
    if 'addr:city' in tags:
        parts.append(tags['addr:city'])
    if 'addr:postcode' in tags:
        parts.append(tags['addr:postcode'])
    return ", ".join(parts) if parts else ""

def get_description(brand, name):
    if "Cafe" in brand:
        return f"A local {brand.lower()} offering coffee and pastries."
    elif "Restaurant" in brand:
        return f"A neighborhood {brand.lower()} serving delicious meals."
    elif "Bar" in brand:
        return f"A cozy {brand.lower()} for evening drinks."
    elif "Shop" in brand:
        return f"A local {brand.lower()} offering unique goods."
    else:
        return f"A popular local spot in the neighborhood."

def generate_data():
    if not os.path.exists('neighborhoods.json'):
        print("neighborhoods.json not found!")
        return

    with open('neighborhoods.json', 'r') as f:
        neighborhoods = json.load(f)

    for nbhd in neighborhoods:
        filepath = f"data/{nbhd['id']}.json"

        # Check if file has > 0 places to skip and save time/API rate limit
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    if len(data.get(nbhd['dataKey'], [])) > 0:
                        print(f"Skipping {nbhd['name']}, already has data.")
                        continue
                except:
                    pass

        print(f"Fetching data for {nbhd['name']}...")
        lat, lon = nbhd['latLng']
        elements = fetch_places(lat, lon)

        places = []
        for el in elements:
            tags = el.get('tags', {})
            name = tags.get('name')
            if not name:
                continue

            brand_type = "Place"
            if tags.get('amenity') == 'cafe':
                brand_type = "Cafe"
            elif tags.get('amenity') == 'restaurant':
                brand_type = "Restaurant"
            elif tags.get('amenity') == 'bar':
                brand_type = "Bar"
            elif tags.get('shop'):
                brand_type = "Shop"

            address = extract_address(tags)
            if not address:
                address = f"Near {lat:.4f}, {lon:.4f}, Brooklyn, NY"

            desc = get_description(brand_type, name)
            if 'cuisine' in tags:
                desc = f"A local {tags['cuisine'].replace(';', ', ')} {brand_type.lower()}."
            elif 'description' in tags:
                desc = tags['description']

            places.append({
                "brand": brand_type,
                "name": name,
                "address": address,
                "description": desc
            })

            if len(places) >= 50:
                break

        seen = set()
        unique_places = []
        for p in places:
            if p['name'] not in seen:
                seen.add(p['name'])
                unique_places.append(p)

        with open(filepath, 'w') as f:
            json.dump({nbhd['dataKey']: unique_places}, f, indent=2)

        print(f"  Saved {len(unique_places)} places to {filepath}")

        time.sleep(5)

if __name__ == "__main__":
    generate_data()
