import allure

from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):

    @allure.step('Ввод электронной почты в поле Email')
    def enter_email(self, email):
        self.add_text_to_element(RecoveryPasswordPageLocators.INPUT_EMAIL_FOR_RECOVERY_FLD, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_btn(self):
        self.click_on_element(RecoveryPasswordPageLocators.RECOVER_BTN)

    @allure.step('Проверка поля ввода кода для восстановления пароля')
    def check_for_enter_code_from_email_field(self):
        return self.get_text_from_element(RecoveryPasswordPageLocators.CODE_FROM_EMAIL_ENTER_FLD)

    @allure.step('Клик по иконке Показать пароль')
    def click_to_show_password(self):
        self.click_on_element(RecoveryPasswordPageLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка активности поля ввода Пароль')
    def check_for_active_password_fld(self):
        return self.check_visibility_of_element(RecoveryPasswordPageLocators.ACTIVE_ENTER_PASSWORD_FLD)

    @allure.step('Получение адреса URL страницы Восстановления пароля')
    def get_url_recovery_page(self):
        return self.get_url()

    @allure.step('Получение текста заголовка "Восстановление пароля"')
    def get_title_of_recovery_password_page(self):
        return self.get_text_from_element(RecoveryPasswordPageLocators.RECOVERING_PASSWORD_TTL)