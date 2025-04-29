# pages/login_page.py
from playwright.sync_api import Page
from config import BASE_URL  # Import base URL from config.py


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL  # Use the central base URL from config.py
        # Define locators
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.login_error = self.page.locator("h3")
        self.url = f"{self.base_url}/"
        # Automatically navigate to the login page when the class is initialized
        # self.page.goto(f"{self.base_url}/")

    def assert_page(self):
        """Ensure the login page is displayed."""
        assert self.username_input.is_visible(), "Username input is not visible"
        assert self.password_input.is_visible(), "Password input is not visible"
        assert self.login_button.is_visible(), "Login button is not visible"
