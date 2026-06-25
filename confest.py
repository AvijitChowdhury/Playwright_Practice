import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()