import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть сайт Tutu.ru и дождаться загрузки")
    def open(self) -> None:
        """
        Эта функция открывает сайт и окно для авторизации
        """
        self.driver.get("https://www.tutu.ru/")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Войти"])[1]'))
        )

    @allure.step("Перейти в окошко регистрации")
    def enter(self) -> None:
        """
        Эта функция нажимает на кнопки Входа и Регистрации
        """
        self.driver.find_element(By.XPATH, '(//span[text()="Войти"])[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="registration-link"]').click()

    @allure.step("Ввести в поле почту {name_mail}")
    def input_mail(self, name_mail: str = 'ivansidorov@1nhm.com') -> None:
        """
        Эта функция вводит в поле почту
        """
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="email-field"]').send_keys(name_mail)

    @allure.step("Включить чекбокс")
    def checkbox(self) -> None:
        """
        Эта функция включает обязательный чекбокс
        """
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="agreement-checkbox"]').click()

    @allure.step("Нажать на кнопку Зарегистрироваться")
    def sign(self) -> None:
        """
        Эта функция нажимает на кнопку Зарегистрироваться
        """
        self.driver.find_element(By.CSS_SELECTOR, '[data-ti="submit-trigger"]').click()

    @allure.step("Дождаться и получить сообщение о принятии почты")
    def check_mail(self) -> str:
        """
        Эта функция дожидается сообщения об отправке кода на почту
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Введите одноразовый код для быстрой регистрации, отправленный на вашу почту."]'))
        )
        mail = self.driver.find_element(
            By.XPATH, '//span[text()="Введите одноразовый код для быстрой регистрации, отправленный на вашу почту."]').text
        return mail

    @allure.step("Дождаться и получить сообщение об ошибке")
    def error_without_mail(self) -> str:
        """
        Эта функция дожидается сообщения об ошибке
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti-error="email"]'))
        )
        error_w_m = self.driver.find_element(
            By.CSS_SELECTOR, '[data-ti-error="email"]').text
        print(error_w_m)
        return error_w_m

    @allure.step("Дождаться и получить сообщение об ошибке")
    def error_without_checkbox(self) -> str:
        """
        Эта функция дожидается сообщения об ошибке
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ti-error="agreement"]'))
        )
        error_w_c = self.driver.find_element(
            By.CSS_SELECTOR, '[data-ti-error="agreement"]').text
        print(error_w_c)
        return error_w_c
