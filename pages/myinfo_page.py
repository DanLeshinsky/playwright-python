import allure

from pages.base_page import BasePage
from config.links import Links
from playwright.sync_api import expect, Page


class MyinfoPage(BasePage):
    PAGE_URL = Links.MYINFO_PAGE

    def __init__(self, page: Page):
        super().__init__(page)
        self.__employee_full_name = self.page.locator('//input[@name="firstName"]')
        self.__save_button = self.page.locator("(//button[@type='submit'])[1]")

    @allure.step("Verify myinfo page open")
    def verify_myinfo_open(self):
        self.validate_page_url()

    @allure.step("Enter new employee full name")
    def enter_new_employee_full_name(self, new_name):
        self.clear_text_from_element(self.__employee_full_name)
        expect(self.__employee_full_name).to_be_empty()
        self.fill_text_to_element(self.__employee_full_name, new_name)
        self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.click_on_element(self.__save_button)

    @allure.step("Verify changes were saved")
    def verify_changes_saved_with(self, new_name):
        expect(self.__employee_full_name).to_have_value(new_name)

    @allure.step("Clear employee full name")
    def clear_employee_full_name(self):
        self.clear_text_from_element(self.__employee_full_name)
        expect(self.__employee_full_name).to_be_empty()

    @allure.step("Change full name")
    def change_name(self, new_name: str) -> str:
        self.type_text_to_element(self.__employee_full_name, new_name)
        return new_name
