from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.button_login = page.get_by_role("button", name="Login")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.button_login.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()