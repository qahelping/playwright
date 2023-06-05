import allure
import playwright.sync_api

from pageobject import MainPage


@allure.title("Open main page")
def test_main_page(page):
    main_page = MainPage(page)

    main_page.navigate()
    main_page.expectMainPageIsOpened()


@allure.title("Click on Get started")
def test_click_on_get_started_page(page):
    main_page = MainPage(page)

    main_page.navigate()
    main_page.click_on_get_started()
    main_page.expectInstallationPageIsOpened()
