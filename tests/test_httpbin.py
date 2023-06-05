import allure

from serviceobject import HttpbinService, HttpbinRequestsService


@allure.title("Api_request_context")
def test_api_request_context(api_request_context):
    httpbin = HttpbinService(api_request_context)

    httpbin.delete()


@allure.title("Requests")
def test_requests_httpbin(api_request_context):
    httpbin = HttpbinRequestsService()

    httpbin.delete()
