import pytest
from playwright.sync_api import sync_playwright
from utils.logging_utils import setup_logger

# Setup Logger
logger = setup_logger("framework")


# Fixture for Playwright instance (Sync)
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


# Fixture for browser (Sync)
@pytest.fixture(scope="session")
def browser(playwright_instance):
    """
    Launch a Chromium browser in headful mode to avoid sync/async issues.
    We ensure we're using the sync version of Playwright.
    """
    # Set headless to False to run in headful mode and see the browser interaction
    headless = False  # Set to False for headful mode
    slowmo = 100  # Slow down the actions by 100ms for better debugging

    # Launch the browser in sync mode
    browser = playwright_instance.chromium.launch(headless=headless, slow_mo=slowmo)
    yield browser
    browser.close()  # Ensure to close the browser after the test session


# Fixture for page (Sync)
@pytest.fixture(scope="function")
def page(browser):
    """
    Create a new context and page for each test function.
    This ensures tests are isolated with fresh state each time.
    """
    # Use the sync browser to create a new context and page
    context = browser.new_context(record_video_dir="reports/videos")
    page = context.new_page()
    yield page
    context.close()  # Close the context after the test finishes to clean up
