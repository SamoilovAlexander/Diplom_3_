import time

import allure

from pages import orders_list_page
from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestOrdersListPage:

    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_opening_details_any_order(self, create_order):
        main_page = MainPage(create_order)
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        order_list_page = OrderListPage(create_order)
        order_list_page.click_on_last_order_card()
        assert order_list_page.get_title_of_popup_with_order_details() == 'Cостав'

    @allure.title('Проверка отображения заказа пользователя из "Истории заказов" в общем списке Ленты заказов')
    def test_displaying_orders_on_orders_history_and_orders_list_pages(self, create_order):
        main_page = MainPage(create_order)
        main_page.get_order_number()
        main_page.close_order_popup()
        personal_account_page = PersonalAccountPage(create_order)
        order_list_page = OrderListPage(create_order)
        main_page.click_on_list_of_orders_btn()
        order_number_main_page = order_list_page.get_order_number_in_list()
        main_page.click_on_personal_account_btn()
        personal_account_page.click_on_orders_history_btn()
        order_number_from_account_page = personal_account_page.get_number_of_last_order()
        assert order_number_from_account_page[1] in order_number_main_page

    @allure.title('Проверка увеличения значения счетчика "Выполнено за все время" после создания нового заказа')
    def test_increase_counter_for_all_time_after_order(self, login_user):
        main_page = MainPage(login_user)
        order_list_page = OrderListPage(login_user)
        main_page.click_on_list_of_orders_btn()
        old_value_of_counter = order_list_page.get_all_time_orders()
        main_page.click_on_constructor_btn()
        main_page.creating_order()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        new_value_of_counter = order_list_page.get_all_time_orders()
        assert new_value_of_counter > old_value_of_counter

    @allure.title('Проверка увеличения значения счетчика "Выполнено за сегодня" после создания нового заказа')
    def test_increase_counter_for_today_after_order(self, login_user):
        main_page = MainPage(login_user)
        order_list_page = OrderListPage(login_user)
        main_page.click_on_list_of_orders_btn()
        old_value_of_counter = order_list_page.get_today_orders()
        main_page.click_on_constructor_btn()
        main_page.creating_order()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        new_value_of_counter = order_list_page.get_today_orders()
        assert new_value_of_counter > old_value_of_counter

    @allure.title('Проверка отображения последнего заказа в блоке номеров заказов "В работе"')
    def test_displaying_order_number_in_in_progress_unit(self, create_order):
        main_page = MainPage(create_order)
        order_number = main_page.get_order_number()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        order_list_page = OrderListPage(create_order)
        in_progress_unit = order_list_page.get_orders_numbers_in_progress()
        assert order_number in in_progress_unit