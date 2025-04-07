import allure

from locators.orders_list_page_locators import OrdersListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    @allure.step('Вызов всплывающего окна с деталями заказа при клике на карточку заказа')
    def click_on_last_order_card(self):
        self.click_on_element(OrdersListPageLocators.LAST_ORDER)

    @allure.step('Проверка появления всплывающего окна с деталями заказа')
    def get_title_of_popup_with_order_details(self):
        return self.get_text_from_element(OrdersListPageLocators.COMPOUND_TTL)

    @allure.step('Получение заказов в ленте заказов')
    def get_order_number_in_list(self):
        return self.get_text_from_element(OrdersListPageLocators.LIST_OF_READY_ORDERS)

    @allure.step('Получение поля номеров заказов "В работе"')
    def get_orders_numbers_in_progress(self):
        self.waiting_for_element_to_be_visible(OrdersListPageLocators.ORDERS_IN_PROGRESS)
        return self.get_text_from_element(OrdersListPageLocators.ORDERS_IN_PROGRESS)

    @allure.step('Получение количества выполненных заказов за всё время')
    def get_all_time_orders(self):
        return self.get_text_from_element(OrdersListPageLocators.ALL_TIME_ORDERS)

    @allure.step('Получение количества выполненных заказов за сегодня')
    def get_today_orders(self):
        return self.get_text_from_element(OrdersListPageLocators.TODAY_ORDERS)

    @allure.step('Получение заголовка страницы "Лента заказов')
    def get_list_of_orders_ttl(self):
        return self.get_text_from_element(OrdersListPageLocators.LIST_OF_ORDERS_TTL)
