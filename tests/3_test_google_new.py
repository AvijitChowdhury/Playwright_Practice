import re
import pytest
from playwright.sync_api import Page, expect

# Automatically navigate to the official Playwright demo app before every test
@pytest.fixture(autouse=True)
def setup_and_navigate(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")

def test_homepage_loads_successfully(page: Page):
    # Verify the title and the main input box
    expect(page).to_have_title(re.compile(r"TodoMVC"))
    
    # Locate elements using placeholder text
    new_todo_input = page.get_by_placeholder("What needs to be done?")
    expect(new_todo_input).to_be_visible()

def test_add_a_new_todo_item(page: Page):
    # Locate the input box
    new_todo_input = page.get_by_placeholder("What needs to be done?")
    
    # Type out the task and hit enter
    new_todo_input.fill("Learn Playwright in Python")
    new_todo_input.press("Enter")

    # Playwright provides `get_by_test_id` for highly stable locators
    todo_items = page.get_by_test_id("todo-item")
    
    # Assert that exactly 1 item was added to the list
    expect(todo_items).to_have_count(1)
    
    # Assert that the text matches what we typed
    expect(todo_items.first).to_have_text("Learn Playwright in Python")

def test_mark_todo_as_completed(page: Page):
    # Setup: Create an item first
    new_todo_input = page.get_by_placeholder("What needs to be done?")
    new_todo_input.fill("Master Test Automation")
    new_todo_input.press("Enter")

    # Locate the specific item and its checkbox
    todo_item = page.get_by_test_id("todo-item").first
    checkbox = todo_item.get_by_role("checkbox")
    
    # Action: Click the checkbox
    checkbox.check()

    # Assert: Verify the UI updated to show it is checked
    expect(checkbox).to_be_checked()
    
    # Assert: Verify the text gets a strikethrough (completed class)
    expect(todo_item).to_have_class(re.compile(r"completed"))