import json
import urllib.parse
from pathlib import Path
from playwright.sync_api import sync_playwright

def run_update():
    neighborhoods_file = Path("neighborhoods.json")
    if not neighborhoods_file.exists():
        print(f"Error: {neighborhoods_file} not found.")
        return

    with open(neighborhoods_file, "r") as f:
        neighborhoods = json.load(f)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        for target_neighborhood in neighborhoods:
            data_file = Path(target_neighborhood["file"].lstrip("/"))
            if not data_file.exists():
                print(f"Skipping {data_file}: File not found.")
                continue

            print(f"Updating {data_file}...")

            with open(data_file, "r") as f:
                data = json.load(f)

            data_key = target_neighborhood.get("dataKey", "places")
            places = data.get(data_key, [])

            final_places = []

            for place in places:
                name = place.get("name", "")
                address = place.get("address", "")

                # Make a search query for Google Maps
                search_query = f"{name} {address}".strip()
                if not search_query:
                    continue

                encoded_query = urllib.parse.quote(search_query)
                search_url = f"https://www.google.com/maps/search/{encoded_query}"

                print(f"Searching for: {search_query}")

                try:
                    page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
                    page.wait_for_timeout(3000)

                    # Try to extract description from the place details pane
                    script = """
                    () => {
                        let elements = document.querySelectorAll('.fontBodyMedium, .fontBodyLarge');
                        for (let el of elements) {
                            let text = el.innerText.trim();
                            // Look for typical editorial summary patterns or decent length descriptions
                            if (text.length > 20 && !text.includes('·') && !text.match(/^\\d{1,2}:\\d{2}/) && !text.match(/^\\+\\d/) && !text.includes('facebook.com') && !text.includes('instagram.com')) {
                                return text;
                            }
                        }

                        let spans = Array.from(document.querySelectorAll('span')).filter(s => s.innerText.length > 30);
                        for (let s of spans) {
                            let t = s.innerText.trim();
                            // Also try to find descriptions ending with a period or general long text that looks like a description.
                            if (!t.includes('·') && !t.match(/^\\d{1,2}:\\d{2}/) && !t.includes('Reviews') && !t.includes('http')) {
                                return t;
                            }
                        }

                        // Try fetching top review text
                        let reviewElements = document.querySelectorAll('.MyEned');
                        for (let r of reviewElements) {
                            let rText = r.innerText.trim();
                            if (rText.length > 20) {
                                return "Known for: " + rText.split('\\n')[0].substring(0, 100) + "...";
                            }
                        }

                        return null;
                    }
                    """
                    description = page.evaluate(script)

                    if description:
                        place["description"] = description
                        final_places.append(place)
                        print(f"Found description: {description}")
                    else:
                        print(f"No description found for {search_query}. Removing place.")
                        # Even if not found, we will append it for now to avoid deleting test data
                        # Wait, the prompt says "If they are not known for anything then don't put this list item here."
                        # However, since this is test data and my Playwright scraper might fail to find real elements on mocked places,
                        # I'll just skip adding it to final_places as requested.

                except Exception as e:
                    print(f"Error fetching {search_query}: {e}")
                    print(f"Removing {name} due to error.")

            data[data_key] = final_places

            with open(data_file, "w") as f:
                json.dump(data, f, indent=2)

            print(f"Successfully updated {data_file} with {len(final_places)} places.")

        browser.close()

if __name__ == "__main__":
    run_update()
