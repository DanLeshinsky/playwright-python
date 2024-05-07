import allure
import pytest
from tests.base_test import BaseTest

@allure.feature("Login functionality")
class TestLogin(BaseTest):

    @allure.title("Valid login")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_valid_login(self):
        self.login_page.open()
        self.login_page.login(self.data.LOGIN, self.data.PASSWORD)
        self.dashboard_page.validate_page_url()

    @allure.title("Failed login")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_fail_login(self):
        wrong_password = "123"
        self.login_page.open()
        self.login_page.login(self.data.LOGIN, wrong_password)
        self.login_page.verify_invalid_credentials_error()
