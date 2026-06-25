"""
Data-driven testing with JSON file
"""
from playwright.sync_api import Page, expect
import pytest
import json
import os

# Get the correct file path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
file_path = os.path.join(project_root, "test_data", "data.json")

def get_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [(item['username'], item['password']) for item in data]

# Get test data
test_data = get_json_data(file_path)

@pytest.mark.parametrize("username, password", test_data)
def test_login_with_json(page: Page, username: str, password: str) -> None:
    """Test login with data from JSON file"""
    print(f"\nTesting: {username}/{password}")
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
    if username == "Admin" and password == "admin123":
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    else:
        error_message = page.locator(".oxd-alert-content")
        expect(error_message).to_be_visible()