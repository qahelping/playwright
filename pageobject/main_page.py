import allure
from playwright.sync_api import expect

from utils.consts import BASE_URL
from allure import attachment_type

class MainPage:

    def __init__(self, page):
        self.page = page
        self.title = page.locator('.hero__title')
        self.get_started = page.locator("[class^='getStarted']")
        self.container = page.locator(".container.padding-top--md.padding-bottom--lg")

    @allure.step("Navigate to main page")
    def navigate(self):
        self.page.goto(BASE_URL)

    @allure.step("Click on Get started")
    def click_on_get_started(self):

        self.get_started.click()

    @allure.step("Expect that main page is opened")
    def expectMainPageIsOpened(self):
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright ")
        expect(self.title).to_be_visible()

    @allure.step("Expect that installation page is opened")
    def expectInstallationPageIsOpened(self):
        self.container.wait_for()
        expect(self.container).to_be_visible()
        expect(self.page).to_have_title("Installation | Playwright")
