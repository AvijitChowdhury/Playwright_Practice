# documentation how to use a

from playwright.sync_api import Page
import pytest
import json
file_path = "./test_data/data.csv"
def get_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            data.append((username, password))
    return data
def get_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [(item['username'], item['password']) for item in data]
# @pytest.mark.parametrize("username, password", [
#     ("Admin", "admin123"),
#     ("Admin", "wrongpassword"),
#     ("wronguser", "admin123"),
# ])
# @pytest.mark.parametrize("username, password", get_csv_data(file_path))
# def test_example(page: Page, username, password) -> None:
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.get_by_role("textbox", name="Username").click()
#     page.get_by_role("textbox", name="Username").fill(username)
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill(password)
#     page.get_by_role("button", name="Login").click()
@pytest.mark.parametrize("Username, Password", get_json_data(file_path))
def test_example(page: Page, Username: str, Password: str) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(Username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(Password)
    page.get_by_role("button", name="Login").click()