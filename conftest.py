import json
from pathlib import Path


import pytest
import pytest


def load_login_data():
    file_path = Path("test_data") / "login_credential.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return data["user_credentials"]


@pytest.fixture(params=load_login_data())
def login_data(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--mybrowser",
        action="append",
        default=["chromium"],
        help="Browser to run tests on"
    )


@pytest.fixture(scope="session")
def browser(playwright, request):

    browser_names = request.config.getoption("--mybrowser")

    for browser_name in browser_names:

     if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)

     elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

     elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)

     else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield browser

    browser.close()


@pytest.fixture
def page(browser):

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
