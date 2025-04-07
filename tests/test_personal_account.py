import allure

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет по клику по одноименной кнопке в заголовке страницы')
    def test_go_to_personal_account_by_click_this_btn(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_on_personal_account_btn()
        personal_account_page = PersonalAccountPage(login_user)
        assert personal_account_page.check_visibility_of_element(PersonalAccountPageLocators.PROFILE_BTN)

    @allure.title('Проверка перехода в раздел "История заказов" по клику по одноименной кнопке в личном кабинете')
    def test_go_to_history_of_orders_by_click_this_btn(self, login_user):
        main_page = MainPage(login_user)
        personal_account_page = PersonalAccountPage(login_user)
        main_page.click_on_personal_account_btn()
        personal_account_page.click_on_orders_history_btn()
        assert personal_account_page.check_visibility_of_element(PersonalAccountPageLocators.COMPLETED_TITLE)

    def test_logout_from_account(self, login_user):
        main_page = MainPage(login_user)
        personal_account_page = PersonalAccountPage(login_user)
        main_page.click_on_personal_account_btn()
        personal_account_page.click_on_logout_btn()
        login_page = LoginPage(login_user)
        title = login_page.get_title_of_login_btn()
        assert 'Войти' == title