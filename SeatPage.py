import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeatPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу с результатами поиска билетов и выбрать поезд")
    def open(self) -> None:
        """
        Эта функция открывает страницу с результатами поиска билетов на 05.05.2025 по пути Сургут-Тюмень и выбирает поезд 377Г
        """
        self.driver.get('https://www.tutu.ru/poezda/rasp_d.php?nnst1=2030600&nnst2=2030100&date=05.05.2025&travelers=1')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div').click()

    @allure.step("Увеличить количество пассажиров и получить результат изменения")
    def check_number(self) -> str:
        """
        Эта функция увеличивает количество взрослых пассажиров от 1 до 2, дожидается изменений на странице
        Возвращает текст полученного результата
        """
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[1]/div[2]/div[3]/button').click()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div[2]/div/div[1]/div/div[1]'))
        )
        number = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div[2]/div/div[1]/div/div[1]/span[1]').text
        return number

    @allure.step("Выбрать вагон, место и дождаться появления стоимости билета")
    def check_price(self) -> str:
        """
        Эта функция нажимает на вагон 2, на место 20 на схеме вагона и получает стоимость билета
        Возвращает стоимость
        """
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[5]/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/div[4]/div/div/div/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[5]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div[21]/div').click()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[6]/div/div/div/div/div/div[2]/div[2]/span/span'))
        )
        price_before = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[4]/div[6]/div/div/div/div/div/div[2]/div[2]/span/span').text
        return price_before

    @allure.step("Отключить чекбокс с услугой и дождаться пересчёта стоимости билета")
    def check_price_without_service(self) -> str:
        """
        Эта функция отключает чекбокс с предоставлением белья и получает новую стоимость билета
        Возвращает пересчитанную стоимость
        """
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[5]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/label/div[1]/input').click()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[6]/div/div/div/div/div/div[2]/div[2]/span/span'))
        )
        price_after = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[4]/div[6]/div/div/div/div/div/div[2]/div[2]/span/span').text
        return price_after
