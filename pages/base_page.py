import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с заложенным ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент с заложенным ожиданием')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание отображения элемента на странице')
    def waiting_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверка наличия элемента на странице')
    def check_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до заданного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение адреса URL текущей страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверка отсутствия элемента на странице')
    def check_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Перетаскивание элемента по странице')
    def drag_and_drop(self, locator_from, locator_to):
        self.waiting_for_element_to_be_visible(locator_from)
        self.waiting_for_element_to_be_visible(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()