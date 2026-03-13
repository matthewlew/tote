import argparse
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def extract_coords(url):
    match = re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', url)
    if match:
        return float(match.group(1)), float(match.group(2))
    match = re.search(r'/@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None, None

def run(list_url, neighborhood_id):
    neighborhoods_file = Path("neighborhoods.json")
    if not neighborhoods_file.exists():
        print(f"Error: {neighborhoods_file} not found.")
        sys.exit(1)

    with open(neighborhoods_file, "r") as f:
        neighborhoods = json.load(f)

    target_neighborhood = next((n for n in neighborhoods if n["id"] == neighborhood_id), None)
    if not target_neighborhood:
        print(f"Error: Neighborhood ID '{neighborhood_id}' not found in {neighborhoods_file}.")
        sys.exit(1)

    data_file = Path(target_neighborhood["file"].lstrip("/"))
    if not data_file.exists():
        with open(data_file, "w") as f:
            data_key = target_neighborhood.get("dataKey", "places")
            json.dump({data_key: []}, f)

    print(f"Updating {data_file} from {list_url}...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        try:
            page.goto(list_url, timeout=60000, wait_until="domcontentloaded")
            page.wait_for_timeout(5000)

            print("Scrolling to load items...")

            # Find the scrollable container and scroll down
            script = """
            () => {
                let container = null;
                let max_scroll = 0;
                for (let el of document.querySelectorAll('div')) {
                    if (el.scrollHeight > el.clientHeight && el.scrollHeight > max_scroll) {
                        max_scroll = el.scrollHeight;
                        container = el;
                    }
                }
                if (container) {
                    window.scrollContainer = container;
                    return true;
                }
                return false;
            }
            """
            found = page.evaluate(script)
            if found:
                print("Found scrollable container. Scrolling...")
                for _ in range(25): # scroll a lot to get all items
                    page.evaluate("() => { window.scrollContainer.scrollTop = window.scrollContainer.scrollHeight; }")
                    page.wait_for_timeout(1000)
            else:
                print("Container not scrollable, falling back to window scrolling")
                for _ in range(15):
                    page.mouse.wheel(0, 5000)
                    page.wait_for_timeout(1000)

            # After scrolling, we have loaded elements
            items_locators = page.query_selector_all('.fontHeadlineSmall')
            print(f"Found {len(items_locators)} items visibly loaded in the list.")

            places = []

            for item in items_locators:
                name = item.inner_text()

                # To make this robust without breaking virtualized scrolling,
                # we just extract name and address from the DOM.
                details = item.evaluate('''el => {
                    let d = [];
                    let p = el.parentElement;
                    if (p && p.parentElement) {
                        let elems = p.parentElement.querySelectorAll('.fontBodyMedium');
                        for (let e of elems) { d.push(e.innerText); }
                    }
                    return d;
                }''')

                address = ", ".join(details).replace("\n", ", ")

                # Try to extract the URL if present in data-url, sometimes it's there
                place_url = item.evaluate('el => { let b = el.closest("button"); return b ? b.getAttribute("data-url") : null; }')

                lat, lng = None, None
                if place_url:
                    lat, lng = extract_coords(place_url)

                places.append({
                    "name": name,
                    "address": address,
                    "latLng": [lat, lng] if lat is not None and lng is not None else [],
                })

            unique_places = {}
            for p in places:
                unique_places[p["name"]] = p

            final_places = list(unique_places.values())

            with open(data_file, "r") as f:
                data = json.load(f)

            data_key = target_neighborhood.get("dataKey", "places")
            data[data_key] = final_places

            with open(data_file, "w") as f:
                json.dump(data, f, indent=2)

            print(f"Successfully updated {data_file} with {len(final_places)} places.")

        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()

        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update a neighborhood JSON file from a Google Maps list.")
    parser.add_argument("url", help="Google Maps List URL")
    parser.add_argument("neighborhood_id", help="ID of the neighborhood to update (e.g. bed_stuy)")

    args = parser.parse_args()
    run(args.url, args.neighborhood_id)
