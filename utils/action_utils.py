from playwright.sync_api import Locator, Page
from helpers import capture_screenshot  # Assuming capture_screenshot is a helper function in your project
from .logging_utils import setup_logger

# Logger setup
logger = setup_logger()


# Function to load the page URL (Sync)
def load_page_url(page: Page, url: str):
    try:
        page.goto(url)
        logger.info(f"[LOAD] Page loaded with URL: {url}")
    except Exception as e:
        path = capture_screenshot(page, "page_load_failed")
        logger.error(f"[FAIL] Failed to load page with URL: {url} | Error: {e} | Screenshot: {path}")
        raise


# Function to get video path if exists (Sync)
def get_video_path(page: Page):
    # Video is stored in the context's record_video_dir
    video_path = page.context.videos[0] if page.context.videos else None
    return video_path


# Generic click action (Sync)
def click_element(page: Page, locator: Locator, description: str = ""):
    try:
        locator.click()
        logger.info(f"[CLICK] {description or locator}")
    except Exception as e:
        path = capture_screenshot(page, "click_failed")
        video_path = get_video_path(page)
        logger.error(
            f"[FAIL] Click failed on {description or locator} | Error: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Fill input field (Sync)
def fill_text(page: Page, locator: Locator, text: str, description: str = ""):
    try:
        locator.fill(text)
        logger.info(f"[FILL] {description or locator} with '{text}'")
    except Exception as e:
        path = capture_screenshot(page, "fill_failed")
        video_path = get_video_path(page)
        logger.error(
            f"[FAIL] Fill failed on {description or locator} | Error: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Select dropdown by visible text (Sync)
def select_dropdown(page: Page, locator: Locator, text: str, description: str = ""):
    try:
        locator.select_option(label=text)
        logger.info(f"[SELECT] {description or locator} -> '{text}'")
    except Exception as e:
        path = capture_screenshot(page, "dropdown_failed")
        video_path = get_video_path(page)
        logger.error(
            f"[FAIL] Select failed on {description or locator} | Error: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Check/Uncheck checkbox (Sync)
def handle_checkbox(page: Page, locator: Locator, action: str = "check", description: str = ""):
    try:
        if action == "check" and not locator.is_checked():
            locator.check()
            logger.info(f"[CHECKED] {description or locator}")
        elif action == "uncheck" and locator.is_checked():
            locator.uncheck()
            logger.info(f"[UNCHECKED] {description or locator}")
        else:
            logger.info(f"[SKIPPED] Checkbox already in desired state: {action}")
    except Exception as e:
        path = capture_screenshot(page, "checkbox_failed")
        video_path = get_video_path(page)
        logger.error(
            f"[FAIL] Checkbox action '{action}' failed | Error: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Handle alerts/modals (Sync)
def handle_alert(page: Page, accept=True, prompt_text=None):
    try:
        def dialog_handler(dialog):
            logger.info(f"[ALERT] Text: {dialog.message}")
            if prompt_text:
                dialog.accept(prompt_text)
            elif accept:
                dialog.accept()
            else:
                dialog.dismiss()

        page.once("dialog", dialog_handler)
        logger.info("[ALERT HANDLER] Attached")
    except Exception as e:
        path = capture_screenshot(page, "alert_failed")
        video_path = get_video_path(page)
        logger.error(f"[FAIL] Alert handling failed | Error: {e} | Screenshot: {path} | Video: {video_path}")
        raise
