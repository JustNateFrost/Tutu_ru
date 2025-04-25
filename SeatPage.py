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
        Эта функция открывает страницу с результатами поиска билетов на 05.05.2025 по пути Сургут-Тюмень
         и выбирает поезд 377Г
        """
        self.driver.maximize_window()
        self.driver.get('https://www.tutu.ru/poezda/rasp_d.php?nnst1=2030600&nnst2=2030100&date=05.05.2025&travelers=1')
        first_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'button[data-ti="main-tariff-content-default"]')
            )
        )[0]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_button)
        first_button.click()


    @allure.step("Увеличить количество пассажиров и получить результат изменения")
    def check_number(self) -> str:
        """
        Эта функция увеличивает количество взрослых пассажиров от 1 до 2, дожидается изменений на странице
        Возвращает текст полученного результата
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//*[@data-ti="order-counter-last-button"])[1]'))
        )
        self.driver.find_element(By.XPATH, '(//*[@data-ti="order-counter-last-button"])[1]').click()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//*[@data-ti="title"])[4]'))
        )
        number = self.driver.find_element(
            By.XPATH, '(//*[@data-ti="title"])[4]').text
        return number

    @allure.step("Выбрать вагон, место и дождаться появления стоимости билета")
    def check_price(self) -> str:
        """
        Эта функция нажимает на вагон 2, на место 20 на схеме вагона и получает стоимость билета
        Возвращает стоимость
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//button[@data-ti="order-button"])[6]'))
        )
        order = self.driver.find_element(By.XPATH, '(//button[@data-ti="order-button"])[6]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order)
        order.click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti-seat="20"]').click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti="next_step_price"]'))
        )
        price_before = self.driver.find_element(
            By.CSS_SELECTOR, '[data-ti="next_step_price"]').text
        return price_before

    @allure.step("Отключить чекбокс с услугой и дождаться пересчёта стоимости билета")
    def check_price_without_service(self) -> str:
        """
        Эта функция отключает чекбокс с предоставлением белья и получает новую стоимость билета
        Возвращает пересчитанную стоимость
        """
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="laundry-checkbox"]').click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti="next_step_price"]'))
        )
        price_after = self.driver.find_element(
            By.CSS_SELECTOR, '[data-ti="next_step_price"]').text
        return price_after
