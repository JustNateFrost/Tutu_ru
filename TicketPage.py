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
        self.driver.get("https://www.tutu.ru/")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div/div/ul/li[4]/button/div/span[2]/span/span'))
        )

    @allure.step("Перейти в раздел Ж/д билетов, выбрать Завтра в качестве даты для поиска билетов")
    def date(self) -> None:
        """
        Эта функция нажимает на кнопку для перехода в раздел поиска Ж/д билетов, выбирает дату завтрашнего дня
        """
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/button[3]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/button[2]').click()

    @allure.step("Ввести в поле Откуда {city_from}")
    def input_from(self, city_from: str = 'Сургут') -> None:
        """
        Эта функция вводит в поле Откуда название города Сургут
        """
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/label/input').send_keys(city_from)

    @allure.step("Ввести в поле Куда {city_to} и нажать на кнопку Выбрать")
    def input_to(self, city_to: str = 'Тюмень') -> None:
        """
        Эта функция вводит в поле Куда название города Тюмень и перейти на страницу с найденными билетами
        """
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/label/input').send_keys(city_to)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/button').click()

    @allure.step("Получить текст с путём следования найденных билетов")
    def check_cities(self) -> str:
        """
        Эта функция получает текст с пунктами отправления и следования для поиска билетов
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/span'))
        )
        cities = self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/span').text
        return cities
