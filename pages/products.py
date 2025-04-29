# pages/login_page.py
from playwright.sync_api import Page
from config import BASE_URL  # Import base URL from config.py

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_page_title = self.page.locator("span.title")
        self.url = f"{BASE_URL}/inventory.html"

    def assert_page(self):
        assert self.products_page_title.inner_text() == "Products"
