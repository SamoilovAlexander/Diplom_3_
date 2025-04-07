import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке Войти в аккаунт')
    def click_on_login_into_account_btn(self):
        self.click_on_element(MainPageLocators.LOGIN_INTO_ACCOUNT_BTN)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_on_personal_account_btn(self):
        self.click_on_element(MainPageLocators.APPHEADER_PERSONAL_ACCOUNT_BTN)

    @allure.step('Клик по кнопке Конструктор')
    def click_on_constructor_btn(self):
        self.click_on_element(MainPageLocators.APPHEADER_CONSTRUCTOR_BTN)

    @allure.step('Клик по кнопке Лента заказов')
    def click_on_list_of_orders_btn(self):
        self.click_on_element(MainPageLocators.APPHEADER_LIST_OF_ORDERS_BTN)

    @allure.step('Скролл до говяжей отбивной')
    def scroll_to_beef_chop(self):
        self.scroll_to_element(MainPageLocators.BEEF_CHOP)

    @allure.step('Скролл до Экзо-Плантаго')
    def scroll_to_ekzo_plantago(self):
        self.scroll_to_element(MainPageLocators.EKZO_PLANTAGO)

    @allure.step('Клик на говяжью отбивную')
    def click_on_beef_chop(self):
        self.click_on_element(MainPageLocators.BEEF_CHOP)

    @allure.step('Клик на краторную булку')
    def click_on_bun_n200i(self):
        self.click_on_element(MainPageLocators.BUN_N200i)

    @allure.step('Проверка заголовка всплывающего окна с деталями ингридиента')
    def check_title_of_popup(self):
        return self.get_text_from_element(MainPageLocators.TITLE_OF_INGREDIENT_POPUP)

    @allure.step('Закрытие всплывающего окна с деталями ингридиента')
    def close_ingredient_popup(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_POPUP_BTN)

    @allure.step('Перетаскивание 1 ингредиента в область заказа для каунтера')
    def move_ingredient_in_order_area_for_counter(self):
        self.drag_and_drop(MainPageLocators.BUN_N200i, MainPageLocators.ORDER_AREA)

    @allure.step('Получение данных (количества) со счётчика ингредиента')
    def get_count_of_ingredient(self):
        return self.get_text_from_element(MainPageLocators.COUNT_OF_BUN_N200i)

    @allure.step('Нажатие на кнопку Оформить заказ')
    def click_create_an_order_btn(self):
        self.click_on_element(MainPageLocators.CREATE_AN_ORDER_BTN)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        self.waiting_for_element_to_be_visible(MainPageLocators.ORDER_ID)
        self.check_invisibility_of_element(MainPageLocators.OVERLAY)
        return self.get_text_from_element(MainPageLocators.ORDER_ID)

    @allure.step('Закрытие всплывающего окна с деталями заказа')
    def close_order_popup(self):
        self.check_invisibility_of_element(MainPageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.CLOSE_ORDER_POPUP_BTN)

    @allure.step('Перетаскивание ингредиента в область заказа')
    def move_ingredient_in_order_area(self):
        time.sleep(2)
        self.drag_and_drop(MainPageLocators.BUN_N200i, MainPageLocators.ORDER_AREA)
        self.drag_and_drop(MainPageLocators.SPICY_X, MainPageLocators.ORDER_AREA)
        self.scroll_to_beef_chop()
        self.drag_and_drop(MainPageLocators.BEEF_CHOP, MainPageLocators.ORDER_AREA)
        self.scroll_to_ekzo_plantago()
        self.drag_and_drop(MainPageLocators.EKZO_PLANTAGO, MainPageLocators.ORDER_AREA)
        self.drag_and_drop(MainPageLocators.CHEESE, MainPageLocators.ORDER_AREA)

    @allure.step('Флоу с созданием заказа')
    def creating_order(self):
        self.move_ingredient_in_order_area()
        self.click_create_an_order_btn()

    @allure.step('Получение текста заголовка страницы конструктора "Соберите бургер"')
    def get_title_of_constructor_page(self):
        return self.get_text_from_element(MainPageLocators.ASSEMBLE_THE_BURGER_TTL)

    @allure.step('Поиск текста заголовка страницы конструктора "Соберите бургер"')
    def find_title_of_constructor_page(self):
        return self.find_element_with_wait(MainPageLocators.ASSEMBLE_THE_BURGER_TTL)

    @allure.step('Получение текста заголовка всплывающего окна с деталями заказа')
    def get_title_of_create_order(self):
        return self.get_text_from_element(MainPageLocators.BEGIN_COOKING_TTL)

