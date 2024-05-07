import allure
from pages.base_page import BasePage
from config.links import Links
from playwright.sync_api import expect


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, page):
        super().__init__(page)
        self.__username = self.page.locator('//input[@name="username"]')
        self.__password = self.page.locator('//input[@name="password"]')
        self.__submit_btn = self.page.locator('//button[@type="submit"]')
        self.__invalid_credentials = self.page.locator("//div[@class='oxd-alert-content oxd-alert-content--error']//p[text()='Invalid credentials']")

    @allure.step("Fill in user name")
    def enter_username(self, user_name):
        self.fill_text_to_element(self.__username, user_name)

    @allure.step("Fill in password")
    def enter_password(self, password):
        self.fill_text_to_element(self.__password, password)

    @allure.step("Click on submit button")
    def submit_login(self):
        self.__submit_btn.click()

    @allure.step("Verify invalid credentials error appears")
    def verify_invalid_credentials_error(self):
        expect(self.__invalid_credentials).to_be_visible()

    def login(self, user_name, password):
        self.enter_username(user_name)
        self.enter_password(password)
        self.submit_login()