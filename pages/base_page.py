import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import expect, Page, Locator


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            if self.PAGE_URL:
                self.page.goto(self.PAGE_URL)
            else:
                print("Not possible to open page without url")

    def validate_page_url(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            expect(self.page).to_have_url(self.PAGE_URL)

    # def check_result_text_is_(self, text):

    def click_on_element(self, element: Locator, timeout=None):
        element.click(timeout=timeout)

    def fill_text_to_element(self, element: Locator, text_to_fill):
        element.fill(text_to_fill)

    def type_text_to_element(self, element: Locator, text: str, delay_ms=400):
        element.type(text, delay=delay_ms)

    def clear_text_from_element(self, element: Locator):
        element.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press('Backspace')

    def attach_screenshot(self, screenshot_name):
        allure.attach(
            body=self.page.screenshot(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
