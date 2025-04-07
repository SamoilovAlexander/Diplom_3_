import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ввод электронной почты в поле Email')
    def enter_email(self, email):
        self.add_text_to_element(LoginPageLocators.INPUT_EMAIL_FOR_LOGIN_FLD, email)

    @allure.step('Ввод пароля в поле Password')
    def enter_password(self, password):
        self.add_text_to_element(LoginPageLocators.INPUT_PASSWORD_FOR_LOGIN_FLD, password)

    @allure.step('Клик по кнопке Войти')
    def click_login_btn(self):
        self.click_on_element(LoginPageLocators.LOGIN_BTN)

    @allure.step('Клик по ссылке Восстановление пароля')
    def click_recovery_password_lnk(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD_LNK)

    @allure.step('Получение текста с кнопки "Войти"')
    def get_title_of_login_btn(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_BTN)