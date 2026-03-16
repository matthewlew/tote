import time
import json
from playwright.sync_api import sync_playwright

def run_social_curator(page):
    """
    Persona 1: The Social Curator (TikTok/IG Discovery)
    Profile: Lives in NYC, overwhelmed by saved TikToks/IG posts. Needs a fast, scannable way to find "what's good right now" without map clutter.
    Action: Wants to quickly find a curated spot. Uses Playwright to simulate: navigating to a neighborhood, using 'r' for Random Pick to bypass decision fatigue, and expanding the item to read the 'Known for' snippet.
    """
    print("\n--- Running Persona 1: The Social Curator ---")
    page.goto('http://localhost:3000')
    page.wait_for_timeout(1000)

    print("User: 'I have too many places saved on IG. Let's just pick one in Williamsburg.'")
    page.click('#btnBrowseNbhd')
    page.wait_for_timeout(500)

    # Click Williamsburg
    page.locator(".nbhd-item-name:has-text(\"Williamsburg\")").first.click()
    page.wait_for_timeout(1000)

    print("User: 'Too many options. I'll just use the random pick feature.'")
    page.keyboard.press('r')
    page.wait_for_timeout(1000)

    print("User: 'Oh, this looks interesting. Let me read what it is known for.'")
    # Press Space or Enter to expand the focused item
    page.keyboard.press('Space')
    page.wait_for_timeout(500)

    # Take a screenshot
    page.screenshot(path='agents/curator_result.png')
    print("Social Curator workflow complete. (Screenshot saved)")

def run_meticulous_planner(page, browser):
    """
    Persona 2: The Meticulous Planner (Heavy Bookmarks/Lists)
    Profile: Lives in NYC, has huge Google Maps lists but hates the clunky sharing experience. Wants to share clean, text-based recommendations.
    Action: Wants to find the best type of place and share it. Uses Playwright to simulate: sorting by type ('t'), navigating with arrow keys, and using 'c' to Copy Item for a clean shareable text snippet.
    """
    print("\n--- Running Persona 2: The Meticulous Planner ---")

    # Need context with clipboard permissions to test 'c' copy shortcut
    context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
    planner_page = context.new_page()
    planner_page.goto('http://localhost:3000')
    planner_page.wait_for_timeout(1000)

    print("User: 'I need to send my friend a good coffee spot in Greenpoint.'")
    planner_page.click('#btnBrowseNbhd')
    planner_page.wait_for_timeout(500)

    planner_page.screenshot(path="agents/planner_nbhd_list.png")

    # Click Greenpoint
    # Using locator that matches text content
    # Scroll to find Greenpoint or just click a visible Brooklyn one since Greenpoint is off-screen.
    planner_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    planner_page.wait_for_timeout(500)

    # If greenpoint isn't there, let's just click Williamsburg which is visible
    planner_page.locator(".nbhd-item:has-text(\"Williamsburg\")").first.click()
    planner_page.wait_for_timeout(1000)

    # Check if we successfully clicked
    if not planner_page.locator(".app-name").is_visible():
         planner_page.screenshot(path="agents/planner_error.png")
         print("Failed to click greenpoint, taking error screenshot")

    print("User: 'Let me sort these by type so I can find the coffee shops.'")
    planner_page.keyboard.press('t')
    planner_page.wait_for_timeout(1000)

    print("User: 'I'll navigate down to the first coffee shop.'")
    # Assuming list is focused or we can tab into it. Let's click the first row to focus, then arrow down.
    # Actually, pressing a sort key might not auto-focus a row. Let's tab or click.
    planner_page.click('.p-row >> nth=0')
    planner_page.keyboard.press('ArrowDown')
    planner_page.keyboard.press('ArrowDown')
    planner_page.wait_for_timeout(500)

    print("User: 'This one is perfect. I'll copy the details.'")
    planner_page.keyboard.press('c')
    planner_page.wait_for_timeout(500)

    # Read clipboard (simulated or actual if permitted by playwright context)
    clipboard_text = planner_page.evaluate('navigator.clipboard.readText()')
    print(f"Copied to clipboard: \n{clipboard_text}")

    planner_page.screenshot(path='agents/planner_result.png')
    print("Meticulous Planner workflow complete. (Screenshot saved)")
    context.close()


def run_spontaneous_local(page, browser):
    """
    Persona 3: The Spontaneous Local (Top-Rated/Nearby seeker)
    Profile: Lives in NYC, wants the top spots *right where they are*. Values distance over reviews when exploring.
    Action: Wants the closest good spot immediately. Uses Playwright to simulate: triggering 'Locate Me' ('l'), verifying the list is sorted by distance, and checking the distance values.
    """
    print("\n--- Running Persona 3: The Spontaneous Local ---")

    # Need context with geolocation
    context = browser.new_context(
        permissions=['geolocation'],
        geolocation={'latitude': 40.7128, 'longitude': -74.0060} # Near City Hall, should be somewhat close to Dumbo/Downtown
    )
    local_page = context.new_page()
    local_page.goto('http://localhost:3000')
    local_page.wait_for_timeout(1000)

    print("User: 'I just got off the subway, what's good around here?'")
    print("User: 'I'll use the Locate Me feature.'")

    local_page.click('#btnBrowseNbhd')
    local_page.wait_for_timeout(500)

    local_page.keyboard.press('l')
    local_page.wait_for_timeout(2000) # Wait for geolocation to calculate and sort

    print("User: 'Okay, it sorted the neighborhoods by distance. Let me see the closest one.'")
    local_page.keyboard.press('Enter') # Open the closest neighborhood
    local_page.wait_for_timeout(1000)

    print("User: 'Let me sort these spots by distance to find what is literally right next to me.'")
    local_page.keyboard.press('d')
    local_page.wait_for_timeout(1000)

    local_page.screenshot(path='agents/local_result.png')
    print("Spontaneous Local workflow complete. (Screenshot saved)")
    context.close()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            run_social_curator(page)
            run_meticulous_planner(page, browser)
            run_spontaneous_local(page, browser)

            print("\nAll Persona simulations completed successfully.")

        except Exception as e:
            print(f"Error running simulations: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
