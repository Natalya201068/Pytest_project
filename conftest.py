import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--user_language', action='store', default=None,
                     help="Choose user_language: en/ru/es...(etc)")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("user_language")
    my_proxy = os.getenv("MY_PROXY")
    options = Options()
    options.add_argument(f"--proxy-server={my_proxy}")
    options.add_experimental_option('prefs', {
                                    'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
