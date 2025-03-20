import pytest
from selenium import webdriver

from data import PersonalData, Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['Chrome', 'Firefox']) #
def driver(request):
    browser = request.param
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Unsupported browser: {browser}')
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login_user(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    main_page = MainPage(driver)
    main_page.click_on_login_into_account_btn()
    login_page = LoginPage(driver)
    login_page.enter_email(PersonalData.EMAIL)
    login_page.enter_password(PersonalData.PASSWORD)
    login_page.click_login_btn()
    return driver

@pytest.fixture(scope='function')
def create_order(login_user):
    main_page = MainPage(login_user)
    main_page.creating_order()
    return login_user