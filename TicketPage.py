import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TicketPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть сайт Tutu.ru и дождаться загрузки")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.maximize_window()
        self.driver.get("https://www.tutu.ru/")

    @allure.step("Перейти в раздел Ж/д билетов, выбрать Завтра в качестве даты для поиска билетов")
    def date(self) -> None:
        """
        Эта функция нажимает на кнопку для перехода в раздел поиска Ж/д билетов, выбирает дату завтрашнего дня
        """
        self.driver.find_element(By.XPATH, '(//span[text()="Ж/д билеты"])[3]').click()
        self.driver.find_element(By.XPATH, '(//div[text()="Завтра"])[1]').click()

    @allure.step("Заполнить поля Откуда и Куда, нажать на кнопку Выбрать")
    def input(self) -> None:
        """
        Эта функция выбирает из предложенных вариантов города для полей Откуда и Куда, нажимает на кнопку, чтобы перейти на страницу с найденными билетами
        """
        self.driver.find_element(By.XPATH, '(//button[@data-ti="fromHint"])[1]').click()
        self.driver.find_element(By.XPATH, '(//button[@data-ti="fromHint"])[3]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="submit-button"]').click()

    @allure.step("Получить текст с путём следования найденных билетов")
    def check_cities(self) -> str:
        """
        Эта функция получает текст с пунктами отправления и следования для поиска билетов
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti="route"]'))
        )
        cities = self.driver.find_element(
            By.CSS_SELECTOR, '[data-ti="route"]').text
        return cities
