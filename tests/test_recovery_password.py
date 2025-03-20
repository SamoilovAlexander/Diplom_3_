import allure

from data import Urls, PersonalData
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage


class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановление пароля"')
    def test_go_to_recovery_password_page(self, driver):
        driver.get(Urls.LOGIN_PAGE_URL)
        login_page = LoginPage(driver)
        login_page.click_recovery_password_lnk()
        recovery_password_page = RecoveryPasswordPage(driver)
        title = recovery_password_page.get_title_of_recovery_password_page()
        assert 'Восстановление пароля' == title

    @allure.title('Проверка ввода email и клика по кнопке "Восстановить"')
    def test_enter_email_and_click_recovery_btn(self, driver):
        driver.get(Urls.RECOVERY_PASSWORD_PAGE_URL)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.enter_email(PersonalData.EMAIL)
        recovery_password_page.click_recovery_btn()
        assert 'Введите код из письма' == recovery_password_page.check_for_enter_code_from_email_field()

    @allure.title('Проверка активности поля ввода нового пароля при клике по иконке "Показать/скрыть пароль"')
    def test_visibility_of_new_password(self, driver):
        driver.get(Urls.RECOVERY_PASSWORD_PAGE_URL)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.enter_email(PersonalData.EMAIL)
        recovery_password_page.click_recovery_btn()
        recovery_password_page.click_to_show_password()
        assert recovery_password_page.check_for_active_password_fld()