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
        Эта функция открывает сайт
        """
        self.driver.get("https://www.tutu.ru/")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div/div/ul/li[4]/button/div/span[2]/span/span'))
        )

    @allure.step("Перейти в окошко регистрации")
    def enter(self) -> None:
        """
        Эта функция нажимает на кнопки Входа и Регистрации
        """
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/header/div/div/ul/li[4]/button/div/span[2]/span/span').click()
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/p[2]/button").click()

    @allure.step("Ввести в поле почту {name_mail}, включить чекбокс")
    def input_mail(self, name_mail: str = 'ivansidorov@1nhm.com') -> None:
        """
        Эта функция вводит в поле почту, включает обязательный чекбокс, нажимает на кнопку Зарегистрироваться
        """
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[1]/div/label/input").send_keys(name_mail)
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[2]/label/div/div/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[3]/button/div").click()

    @allure.step("Дождаться и получить сообщение о принятии почты")
    def check_mail(self) -> str:
        """
        Эта функция дожидается сообщения об отправке кода на почту
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div/div/p/span[2]'))
        )
        mail = self.driver.find_element(
            By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div/div/p/span[2]').text
        return mail

    @allure.step("Оставить поле пустым, включить чекбокс")
    def output_mail(self) -> None:
        """
        Эта функция не вводит в поле почту, включает обязательный чекбокс, нажимает на кнопку Зарегистрироваться
        """
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[2]/label/div/div/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[3]/button/div").click()

    @allure.step("Дождаться и получить сообщение об ошибке")
    def check_error(self) -> str:
        """
        Эта функция дожидается сообщения об ошибке
        Возвращает текст полученного сообщения
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[3]/div/span/p'))
        )
        error = self.driver.find_element(
            By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div/div/form/div[3]/div/span/p').text
        return error
