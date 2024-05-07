import allure
from pages.base_page import BasePage
from config.links import Links


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    def __init__(self, page):
        super().__init__(page)
        self.__my_info_button = self.page.locator('//span[text()="My Info" or text()="Mijn Info"]')

    @allure.step("Click my info section")
    def click_myinfo_section(self):
        self.click_on_element(self.__my_info_button)
