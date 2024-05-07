import pytest
from playwright.sync_api import Page


@pytest.fixture()
def page(request, context):
    request.cls.page: Page = context.new_page()
    request.cls.page.set_viewport_size({'height': 1080, 'width': 1920})
    yield request.cls.page
