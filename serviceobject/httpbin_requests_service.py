import requests
import allure


class HttpbinRequestsService:

    @allure.step("METHOD: DELETE")
    def delete(self):
        path = 'https://httpbin.org/delete'
        response = requests.delete(path)

        assert response.status_code == 200
