from pathlib import Path

import allure
import pytest
from allure import attachment_type
from playwright.sync_api import sync_playwright
from slugify import slugify

@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1023, 'height': 1080})
            page = context.new_page()

            yield page

        with allure.step(f'Закрыть браузер'):
            page.close()
            context.close()
            browser.close()


@pytest.fixture()
def api_request_context():
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(viewport={'width': 1023, 'height': 1080})
            api_request_context = context.request

            yield api_request_context

        with allure.step(f'Закрыть браузер'):
            context.close()
            browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        if report.failed and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure.attach.file(screen_file, name="screenshot",
                               attachment_type=attachment_type.PNG)
        report.extra = extra
