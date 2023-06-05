import allure
from playwright.sync_api import expect

from utils.consts import BASE_URL
from allure import attachment_type

# /headers /status/:code /redirect/:n
class HttpbinService:

    def __init__(self, api_request_context):
        self.request = api_request_context

    @allure.step("METHOD: DELETE")
    def delete(self):
        path = 'https://httpbin.org/delete'
        response = self.request.delete(path)
        assert response.ok