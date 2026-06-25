"""
Testing using POM Page Object Model architecture
"""
from playwright.sync_api import Page, expect
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.orange_hrm_home_page import HomePage
from pages.orange_hrm_login_page import LoginPage
def test_examples(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Test Case 1: Verify login functionality
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    
    # Verify successful login
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    # Test Case 2: Navigate through menu
    home_page.is_upgrade_button_visible()
    home_page.click_admin()
    '''
    For enabling tracing you just need to add the following code snippet in your test file before the test execution starts:
    pytest --trace on
    pytest --trace off
    pytest --trace show
    pytest --trace clear
    for showing the trace.zip, you have to run the following command:
    pytest show-trace location-of-trace.zip
    '''