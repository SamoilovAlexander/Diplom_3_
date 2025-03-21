import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage


class TestMainPageFunctions:

    @allure.title('Проверка перехода из личного кабинета в конструктор бургеров по клику по одноименной кнопке в заголовке страницы')
    def test_go_to_constructor_by_click_this_btn(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_on_personal_account_btn()
        main_page.click_on_constructor_btn()
        assert main_page.get_title_of_constructor_page() == 'Соберите бургер'

    @allure.title('Проверка перехода из главного меню в раздел Лента заказов')
    def test_go_to_orders_list_page(self,login_user):
        main_page = MainPage(login_user)
        main_page.click_on_list_of_orders_btn()
        orders_list_page = OrderListPage(login_user)
        assert orders_list_page.get_list_of_orders_ttl() == 'Лента заказов'

    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента при клике на отдельный ингредиент')
    def test_click_on_ingredient(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_on_bun_n200i()
        assert main_page.check_title_of_popup() == 'Детали ингредиента'

    @allure.title('Еще одна проверка открытия всплывающего окна с деталями ингредиента при клике на отдельный ингредиент'
                  'только в этот раз со скроллом')
    def test_click_on_ingredient_2(self, login_user):
        main_page = MainPage(login_user)
        main_page.scroll_to_beef_chop()
        main_page.click_on_beef_chop()
        assert main_page.check_title_of_popup() == 'Детали ингредиента'

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента при клике на крестик')
    def test_closing_ingredient_popup(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_on_bun_n200i()
        main_page.close_ingredient_popup()
        assert main_page.find_title_of_constructor_page()

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    def test_increase_counter_of_ingredient(self, login_user):
        main_page = MainPage(login_user)
        main_page.move_ingredient_in_order_area_for_counter()
        assert main_page.get_count_of_ingredient() == '2'

    @allure.title('Проверка полного флоу заказа')
    def test_flow_of_order_by_logged_in_user(self, create_order):
        main_page = MainPage(create_order)
        assert main_page.get_title_of_create_order() == 'Ваш заказ начали готовить'
