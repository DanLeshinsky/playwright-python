import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyinfoPage

class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    myinfo_page: MyinfoPage

    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page
        request.cls.data = Data()

        request.cls.login_page = LoginPage(page)
        request.cls.dashboard_page = DashboardPage(page)
        request.cls.myinfo_page = MyinfoPage(page)