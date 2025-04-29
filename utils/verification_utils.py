import logging
from playwright.sync_api import Page, expect
from helpers import capture_screenshot
from .logging_utils import setup_logger

logger = setup_logger()


# Function to get video path if it exists
def get_video_path(page: Page):
    # Ensure that video exists in context and capture the video path
    video_path = page.context.videos[0] if page.context.videos else None
    return video_path


# Validate if the text of the locator matches the expected text
def validate_text(locator, expected_text: str, description: str = ""):
    try:
        expect(locator).to_have_text(expected_text)
        logger.info(f"[VALIDATE TEXT] {description or locator} -> '{expected_text}'")
    except AssertionError as e:
        path = capture_screenshot(locator.page, "validate_text_failed")
        video_path = get_video_path(locator.page)
        logger.error(
            f"[FAIL] {description or locator} | Validation failed: {e} | Expected: '{expected_text}' | Screenshot: {path} | Video: {video_path}")
        raise


# Validate if the locator is visible
def validate_visible(locator, description: str = ""):
    try:
        expect(locator).to_be_visible()
        logger.info(f"[VALIDATE VISIBLE] {description or locator}")
    except AssertionError as e:
        path = capture_screenshot(locator.page, "validate_visible_failed")
        video_path = get_video_path(locator.page)
        logger.error(
            f"[FAIL] {description or locator} | Visibility validation failed: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Validate if the locator is not visible
def validate_not_visible(locator, description: str = ""):
    try:
        expect(locator).not_to_be_visible()
        logger.info(f"[VALIDATE NOT VISIBLE] {description or locator}")
    except AssertionError as e:
        path = capture_screenshot(locator.page, "validate_not_visible_failed")
        video_path = get_video_path(locator.page)
        logger.error(
            f"[FAIL] {description or locator} | Not visible validation failed: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Validate if the checkbox is checked
def validate_checkbox_checked(locator, description: str = ""):
    try:
        expect(locator).to_be_checked()
        logger.info(f"[VALIDATE CHECKED] {description or locator}")
    except AssertionError as e:
        path = capture_screenshot(locator.page, "validate_checked_failed")
        video_path = get_video_path(locator.page)
        logger.error(
            f"[FAIL] {description or locator} | Checked validation failed: {e} | Screenshot: {path} | Video: {video_path}")
        raise


# Validate if the checkbox is unchecked
def validate_checkbox_unchecked(locator, description: str = ""):
    try:
        expect(locator).not_to_be_checked()
        logger.info(f"[VALIDATE UNCHECKED] {description or locator}")
    except AssertionError as e:
        path = capture_screenshot(locator.page, "validate_unchecked_failed")
        video_path = get_video_path(locator.page)
        logger.error(
            f"[FAIL] {description or locator} | Unchecked validation failed: {e} | Screenshot: {path} | Video: {video_path}")
        raise
