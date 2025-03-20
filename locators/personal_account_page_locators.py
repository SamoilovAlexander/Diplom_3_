from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:


    # локатор кнопки "История заказов"
    ORDERS_HISTORY_BTN = By.XPATH, "//a[text()='История заказов']"

    # локатор кнопки "Профиль"
    PROFILE_BTN = By.XPATH, "//a[text()='Профиль']"

    # локатор статуса заказа "Выполнен"
    COMPLETED_TITLE = By.XPATH, "//p[text()='Выполнен']"

    # локатор кнопки "Выход" в личном кабинете
    LOGOUT_BTN = By.XPATH, "//button[text()='Выход']"

    # локатор последнего заказа
    LAST_ORDER = By.XPATH, "//li[last()]/a/div[1]/p[1]" #"//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')])[1]"  #