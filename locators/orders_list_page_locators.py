from selenium.webdriver.common.by import By


class OrdersListPageLocators:


    # локатор последнего заказа
    LAST_ORDER = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]"

    # локатор заголовка "Состав" на всплывающем окне с деталями заказа
    COMPOUND_TTL = By.XPATH, "//p[text()='Cостав']"

    # локатор поля заказов "В работе"
    ORDERS_IN_PROGRESS = By.XPATH, "//*[contains(@class,'orderListReady')]//li[contains(@class,'digits-default')]"

    # локатор списка номеров готовых заказов
    LIST_OF_READY_ORDERS = By.XPATH, "//ul[@class='OrderFeed_orderList__cBvyi']"

    # локатор счетчика заказов за все время
    ALL_TIME_ORDERS = By.XPATH, ("//p[text()='Выполнено за все время:']/following-sibling::"
                                 "p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    # локатор счетчика заказов за сегодняшний день
    TODAY_ORDERS = By.XPATH, ("//p[text()='Выполнено за сегодня:']/following-sibling::"
                              "p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    # локатор на заголовок страницы "Лента заказов"
    LIST_OF_ORDERS_TTL = By.XPATH, "//h1[text()='Лента заказов']"