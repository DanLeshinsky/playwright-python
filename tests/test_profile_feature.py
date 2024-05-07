import time
import allure
import pytest
from faker import Faker
from tests.base_test import BaseTest

fake = Faker()

@allure.feature("Test profile functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Profile Feature")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_profile(self):
        self.login_page.open()
        self.login_page.login(self.data.LOGIN, self.data.PASSWORD)
        self.dashboard_page.validate_page_url()
        self.dashboard_page.click_myinfo_section()
        self.myinfo_page.verify_myinfo_open()
        self.myinfo_page.clear_employee_full_name()
        new_name = self.myinfo_page.change_name(fake.name())
        self.myinfo_page.save_changes()
        self.myinfo_page.verify_changes_saved_with(new_name)
        self.myinfo_page.attach_screenshot("Success")