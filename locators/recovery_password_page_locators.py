from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:


    # локатор на поле ввода электронной почты окна восстановления пароля
    INPUT_EMAIL_FOR_RECOVERY_FLD = By.XPATH, ".//fieldset/div/div/input"

    # локатор кнопки "Восстановить" окна восставновления пароля
    RECOVER_BTN = By.XPATH, ".//button[text()='Восстановить']"

    # локатор поля ввода кода из Email для восстановления пароля
    CODE_FROM_EMAIL_ENTER_FLD = By.XPATH, ".//label[text()='Введите код из письма']"

    # локатор иконки показа введенного пароля
    SHOW_PASSWORD_ICON = By.XPATH, ".//div[contains(@class,'icon-action')]"

    # локатор поля ввода пароля
    ACTIVE_ENTER_PASSWORD_FLD = By.XPATH, "//label[contains(@class,'input__placeholder-focused')]"

    # локатор надписи "Восстановление пароля"
    RECOVERING_PASSWORD_TTL = By.XPATH, ".//h2[text()='Восстановление пароля']"