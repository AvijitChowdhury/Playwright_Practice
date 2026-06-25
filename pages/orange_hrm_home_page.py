from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.link_admin = page.get_by_role("link", name="Admin")
        self.link_pim = page.get_by_role("link", name="PIM")
        self.link_leave = page.get_by_role("link", name="Leave")
        self.link_time = page.get_by_role("link", name="Time")
        self.link_recruitment = page.get_by_role("link", name="Recruitment")
        self.link_my_info = page.get_by_role("link", name="My Info")
        self.link_performance = page.get_by_role("link", name="Performance")
        self.link_dashboard = page.get_by_role("link", name="Dashboard")
        self.link_directory = page.get_by_role("link", name="Directory")
        self.link_maintenance = page.get_by_role("link", name="Maintenance")
        self.link_buzz = page.get_by_role("link", name="Buzz")
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.button_cancel = page.get_by_role("button", name="Cancel")

    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()

    def click_admin(self):
        self.link_admin.click()

    def click_pim(self):
        self.link_pim.click()

    def click_leave(self):
        self.link_leave.click()

    def click_time(self):
        self.link_time.click()

    def click_recruitment(self):
        self.link_recruitment.click()

    def click_my_info(self):
        self.link_my_info.click()

    def click_performance(self):
        self.link_performance.click()

    def click_dashboard(self):
        self.link_dashboard.click()

    def click_directory(self):
        self.link_directory.click()

    def click_maintenance(self):
        self.link_maintenance.click()

    def click_buzz(self):
        self.link_buzz.click()

    def click_cancel_button(self):
        self.button_cancel.click()