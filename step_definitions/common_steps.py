from pytest_bdd import when, parsers, given, then, scenarios
from playwright.sync_api import Page
from pages.page_factory import PageFactory
from utils.action_utils import click_element, fill_text, select_dropdown, handle_checkbox, handle_alert, load_page_url
from utils.logging_utils import setup_logger
from utils.verification_utils import validate_text

scenarios('../features/')

@given(parsers.parse('user loads "{page_name}" page'))
def step_load_page(page, page_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Use sync method
    load_page_url(page, page_object.url)  # <-- Ensure load_page_url is sync

@given(parsers.parse('the "{page_name}" page is loaded'))
@when(parsers.parse('the "{page_name}" page is loaded'))
@then(parsers.parse('the "{page_name}" page is loaded'))
def step_assert_page(page: Page, page_name: str):
    page_object = PageFactory.get_page(page, page_name)
    page_object.assert_page()
    setup_logger().info(f"[PASS] {page_name} page is displayed correctly with all required elements.")

@when(parsers.parse('I click on the "{element_name}" in "{page_name}" page'))
def step_click_element(page: Page, page_name: str, element_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Use sync method
    element = getattr(page_object, element_name)  # <-- Access element directly without snake_case
    click_element(page, locator=element, description=f"{element_name} in {page_name} page")

@when(parsers.parse('I fill "{text}" into the "{element_name}" in "{page_name}" page'))
def step_fill_text(page: Page, text: str, element_name: str, page_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Get the page object
    element = getattr(page_object, element_name)  # <-- Access the element locator
    fill_text(page, element, text, description=f"{element_name} in {page_name} page")

@when(parsers.parse('I select "{option}" from the "{element_name}" dropdown in "{page_name}" page'))
def step_select_dropdown(page: Page, option: str, page_name: str, element_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Use sync method
    element = getattr(page_object, element_name)  # <-- Access element directly without snake_case
    select_dropdown(page, element, option, description=f"{element_name} in {page_name} page")

@when(parsers.parse('I check the "{element_name}" checkbox in "{page_name}" page'))
def step_check_checkbox(page: Page, page_name: str, element_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Use sync method
    element = getattr(page_object, element_name)  # <-- Access element directly without snake_case
    handle_checkbox(page, locator=element, action="check", description=f"{element_name} in {page_name} page")

@when(parsers.parse('I uncheck the "{element_name}" checkbox in "{page_name}" page'))
def step_uncheck_checkbox(page: Page, page_name: str, element_name: str):
    page_object = PageFactory.get_page(page, page_name)  # <-- Use sync method
    element = getattr(page_object, element_name)  # <-- Access element directly without snake_case
    handle_checkbox(page, locator=element, action="uncheck", description=f"{element_name} in {page_name} page")

@when(parsers.parse('I handle the alert and "{action}" it'))
def step_handle_alert(page: Page, action: str):
    handle_alert(page, accept=action.lower() == "accept")

@when(parsers.parse('I handle the alert with text "{prompt_text}"'))
def step_handle_alert_with_prompt(page: Page, prompt_text: str):
    handle_alert(page, prompt_text=prompt_text, accept=True)

@then(parsers.parse('user see "{text}" on the "{element_name}" in "{page_name}" page'))
def step_validate_text(page: Page, text: str, element_name: str, page_name: str):
    page_object = PageFactory.get_page(page, page_name)
    element = getattr(page_object, element_name)
    validate_text(locator=element, expected_text=text, description=f"Validating text for {element_name}")
