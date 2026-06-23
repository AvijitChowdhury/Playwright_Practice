import re
import pytest
from playwright.sync_api import Page, expect

# A fixture that runs before every test automatically (autouse=True)
# This replaces the `beforeEach` hook from the TypeScript version
@pytest.fixture(autouse=True)
def setup_and_navigate(page: Page):
    # Appending ?hl=en forces Google into English
    page.goto("https://www.google.com/?hl=en")
    
    # Handle Google's occasional cookie/consent overlays
    try:
        consent_button = page.locator('button:has-text("Reject all"), button:has-text("Accept all")').first
        if consent_button.is_visible(timeout=3000):
            consent_button.click()
    except Exception:
        pass

def test_google_homepage_loads_successfully(page: Page):
    # Assert the page title
    expect(page).to_have_title(re.compile(r"Google"))

    # Verify the Search text area is visible.
    search_box = page.get_by_role("combobox", name=re.compile(r"Search", re.IGNORECASE))
    expect(search_box).to_be_visible()
    expect(search_box).to_be_editable()

    # Verify the presence of the "Google Search" and "I'm Feeling Lucky" buttons
    search_button = page.get_by_role("button", name="Google Search").first
    lucky_button = page.get_by_role("button", name="I'm Feeling Lucky").first

    expect(search_button).to_be_visible()
    expect(lucky_button).to_be_visible()

def test_perform_search_and_render_results(page: Page):
    search_query = "Playwright testing framework"

    # Locate the search box
    search_box = page.get_by_role("combobox", name=re.compile(r"Search", re.IGNORECASE))
    
    # FIX: Type the query out slowly like a human (100 milliseconds between keystrokes)
    search_box.press_sequentially(search_query, delay=100)
    
    # Wait a tiny bit before pressing enter, just like a human would
    page.wait_for_timeout(500) 
    search_box.press("Enter")

    # Wait for the URL to change and confirm it contains our query parameters
    expect(page).to_have_url(re.compile(r"search"))
    expect(page).to_have_url(re.compile(r"Playwright"))

    # Assert that the title of the new page reflects the search query
    expect(page).to_have_title(re.compile(search_query, re.IGNORECASE))

    # Assert that the search results container is present
    search_results = page.locator("#search")
    expect(search_results).to_be_visible()

    # Verify at least one link to Playwright's official website exists in the results
    playwright_official_link = page.get_by_role("link", name=re.compile(r"Playwright: Fast and reliable", re.IGNORECASE))
    expect(playwright_official_link.first).to_be_visible()

def test_clear_search_input_after_typing(page: Page):
    search_box = page.get_by_role("combobox", name=re.compile(r"Search", re.IGNORECASE))
    
    # Type something into the search bar
    search_box.fill("Automated UI testing")
    expect(search_box).to_have_value("Automated UI testing")

    # Click the clear (X) button that appears after typing
    clear_button = page.get_by_role("button", name=re.compile(r"Clear", re.IGNORECASE))
    clear_button.click()

    # Verify the search box is empty again
    expect(search_box).to_have_value("")