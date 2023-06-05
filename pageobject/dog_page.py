import allure
from playwright.async_api import expect

from utils.consts import DOG_API


class Dog():
    def __init__(self, page):
        self.page = page
        self.img = page.locator("//div[@class='image-content']/img")

    @allure.step("Navigate to main page")
    def navigate(self):
        self.page.goto(DOG_API)

    @allure.step("MOCK: random")
    def handle(route):
        json = {'message': {"test_breed": ['african']}}
        route.fulfill(json=json)



    @allure.step("Expect that main page is opened")
    def expect_img_is_visible(self):
        self.page.wait_for_timeout(5)
        expect(self.img).to_be_visible()
        expect(self.img).to_have_attribute('src', 'https://images.dog.ceo/breeds/appenzeller/n02107908_754.jpg')
