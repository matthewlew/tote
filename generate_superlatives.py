import json
import os
import random
from pathlib import Path

def generate_superlative_lists():
    """
    Reads existing neighborhood data and superlative categories,
    and generates combination JSON lists (e.g., data/williamsburg_dive_bars.json)
    simulating an automated curation process.
    """
    print("Generating automated superlative lists...")

    # Load categories
    try:
        with open('categories.json', 'r') as f:
            categories = json.load(f)
    except FileNotFoundError:
        print("Error: categories.json not found.")
        return

    # Load neighborhoods
    try:
        with open('neighborhoods.json', 'r') as f:
            neighborhoods = json.load(f)
    except FileNotFoundError:
        print("Error: neighborhoods.json not found.")
        return

    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)

    # Process each neighborhood
    for neighborhood in neighborhoods:
        neighborhood_id = neighborhood['id']
        neighborhood_file = data_dir / f"{neighborhood_id}.json"

        # Load neighborhood data to sample from
        neighborhood_data = {"places": []}
        if neighborhood_file.exists():
            try:
                with open(neighborhood_file, 'r') as f:
                    neighborhood_data = json.load(f)
            except json.JSONDecodeError:
                pass

        places = neighborhood_data.get("places", [])

        # If the neighborhood doesn't have enough data to simulate, we'll create placeholders
        # or randomly assign existing places to simulate curating a "Best 100" list.
        for category in categories:
            category_id = category['id']
            intersection_filename = f"{neighborhood_id}_{category_id}.json"
            intersection_filepath = data_dir / intersection_filename

            # Simulate "curation": pick a random subset of places (1 to 5) for this category
            # If places exist. Otherwise just an empty list so the file structure is valid.
            curated_places = []
            if places:
                # Add some randomness to simulate real updates
                sample_size = min(len(places), random.randint(1, max(1, len(places) // 2)))
                if sample_size > 0:
                    curated_places = random.sample(places, sample_size)

            # Save the intersection data
            intersection_data = {
                "places": curated_places
            }

            with open(intersection_filepath, 'w') as f:
                json.dump(intersection_data, f, indent=4)

    print(f"Generated {len(categories) * len(neighborhoods)} automated superlative lists in data/ directory.")

if __name__ == "__main__":
    generate_superlative_lists()
