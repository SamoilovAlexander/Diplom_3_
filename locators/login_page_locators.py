from selenium.webdriver.common.by import By


class LoginPageLocators:

    # локатор на поле ввода электронной почты окна входа
    INPUT_EMAIL_FOR_LOGIN_FLD = By.XPATH, ".//fieldset[1]/div/div/input"

    # локатор на поле ввода пароля окна входа
    INPUT_PASSWORD_FOR_LOGIN_FLD = By.XPATH, ".//fieldset[2]/div/div/input"

    # локатор на кнопку "Войти" окна входа
    LOGIN_BTN = By.XPATH, ".//button[text()='Войти']"

    # локатор на ссылку на восстановление пароля
    RECOVERY_PASSWORD_LNK = By.XPATH, "//a[text()='Восстановить пароль']"