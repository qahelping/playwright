import allure
import playwright.sync_api

from pageobject import Dog


@allure.title("Open main page")
def test_main_page(page):
    main_page = Dog(page)

    page.route("https://dog.ceo/api/breeds/list/all", main_page.handle)
    main_page.navigate()

    main_page.expect_img_is_visible()
