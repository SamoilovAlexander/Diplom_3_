import allure

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Клик по кнопке История заказов')
    def click_on_orders_history_btn(self):
        self.click_on_element(PersonalAccountPageLocators.ORDERS_HISTORY_BTN)

    @allure.step('Клик по кнопке Выход')
    def click_on_logout_btn(self):
        self.click_on_element(PersonalAccountPageLocators.LOGOUT_BTN)

    @allure.step('Получение номера последнего заказа')
    def get_number_of_last_order(self):
        return self.get_text_from_element(PersonalAccountPageLocators.LAST_ORDER)

