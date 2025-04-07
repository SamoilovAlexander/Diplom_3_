from selenium.webdriver.common.by import By


class MainPageLocators:


    # локатор кнопки 'Войти в аккаунт' на главной странице
    LOGIN_INTO_ACCOUNT_BTN = By.XPATH, "//button[text()='Войти в аккаунт']"

    # локатор на кнопку "Личный кабинет" главной страницы
    APPHEADER_PERSONAL_ACCOUNT_BTN = By.XPATH, ".//div/header/nav/a/p[text()='Личный Кабинет']"

    # локатор на заголовок "Конструктор"
    APPHEADER_CONSTRUCTOR_BTN = By.XPATH, "//p[text()='Конструктор']"

    # локатор на заголовок "Лента Заказов"
    APPHEADER_LIST_OF_ORDERS_BTN = By.XPATH, "//p[text()='Лента Заказов']"

    # локатор ингридиента Говяжий метеорит (отбивная)
    BEEF_CHOP = By.XPATH, "//*[@alt='Говяжий метеорит (отбивная)']"

    # локатор ингридиента Краторная булка N-200i
    BUN_N200i = By.XPATH, "//*[@alt='Краторная булка N-200i']"

    # локатор ингредиента Соус Spicy-X
    SPICY_X = By.XPATH, "//*[@alt='Соус Spicy-X']"

    # локатор ингредиента Мини-салат Экзо-Плантаго
    EKZO_PLANTAGO = By.XPATH, "//*[@alt='Мини-салат Экзо-Плантаго']"

    # локатор ингредиента Сыр с астероидной плесенью
    CHEESE = By.XPATH, "//*[@alt='Сыр с астероидной плесенью']"

    # локатор на заголовок всплывающего окна с деталями ингридиента
    TITLE_OF_INGREDIENT_POPUP = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified')]"

    # локатор на кнопку закрыть всплывающего окна с деталями ингридиента
    CLOSE_INGREDIENT_POPUP_BTN = By.XPATH, "//section[1]/div[1]/button[contains(@class,'Modal_modal__close_modified')]"

    # локатор каунтера ингредиента
    COUNT_OF_BUN_N200i = By.XPATH, "//p[contains(@class, 'counter__num') and text()!=0]" #

    # локатор на область конструктора бургера
    ORDER_AREA = By.XPATH, "//*[@class='BurgerConstructor_basket__list__l9dp_']"

    # локатор кнопки Оформить заказ
    CREATE_AN_ORDER_BTN = By.XPATH, "//button[text()='Оформить заказ']"

    # локатор идентификатора заказа
    ORDER_ID = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]"

    # локатор на кнопку закрыть всплывающего окна с деталями ингридиента
    CLOSE_ORDER_POPUP_BTN = By.XPATH, "//button[contains(@type,'button')]"

    OVERLAY = (By.XPATH, '//div/div[@class="Modal_modal_overlay__x2ZCr"]')

    # локатор на заголовок конструктора "Соберите бурер"
    ASSEMBLE_THE_BURGER_TTL = By.XPATH, "//h1[text()='Соберите бургер']"

    # локатор заголовка "Ваш заказ начали готовить" всплывающего окна с деталями заказа
    BEGIN_COOKING_TTL = By.XPATH, "//p[text()='Ваш заказ начали готовить']"