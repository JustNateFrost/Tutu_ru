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

    @allure.step("Открыть страницу с результатами поиска билетов")
    def open(self) -> str:
        """
        Эта функция открывает страницу с результатами поиска билетов на 05.05.2025 по пути Сургут-Тюмень и выбирает поезд 377Г
        Возвращает информацию для поиска билета
        """
        self.driver.maximize_window()
        self.driver.get('https://www.tutu.ru/poezda/rasp_d.php?nnst1=2030600&nnst2=2030100&date=05.05.2025&travelers=1')
        info_before = self.driver.find_element(By.CSS_SELECTOR, '[data-ti="info"]').text
        return info_before

    @allure.step("Изменить дату")
    def change_date(self) -> str:
        """
        Эта функция меняет дату
        Возвращает обновленную информацию для поиска билета
        """
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/div[2]/div[4]').click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti="info"]'))
        )
        info_after = self.driver.find_element(By.CSS_SELECTOR, '[data-ti="info"]').text
        return info_after
