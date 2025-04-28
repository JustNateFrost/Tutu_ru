import allure
import pytest
from selenium import webdriver
from SignPage import SignPage
from TicketPage import TicketPage
from SearchPage import SearchPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Регистрация на сайте через почту")
@allure.description("Проверка ввода и принятия валидной почты для регистрации на сайте")
def test_sign(driver):
    sign_page = SignPage(driver)
    sign_page.open()
    sign_page.enter()
    sign_page.input_mail()
    sign_page.checkbox()
    sign_page.sign()
    mailing = sign_page.check_mail()

    with allure.step("Сравнить полученное сообщение с ожидаемым"):
        assert mailing == "Введите одноразовый код для быстрой регистрации, отправленный на вашу почту."


@allure.epic("UI")
@allure.story("Negative")
@allure.severity("critical")
@allure.title("Оставление поля ввода почты при регистрации пустым")
@allure.description("Ожидание сообщения об ошибке при пустом значении в поле для почты при регистрации на сайте")
def test_no_sign(driver):
    sign_page = SignPage(driver)
    sign_page.open()
    sign_page.enter()
    sign_page.checkbox()
    sign_page.sign()
    sign_page.error_without_mail()
    with allure.step("Дождаться и получить сообщение об ошибке"):
        error_message = sign_page.error_without_mail()

    with allure.step("Сравнить полученное сообщение с ожидаемым"):
        assert error_message == "Без адреса электронной почты никак."


@allure.epic("UI")
@allure.story("Negative")
@allure.severity("critical")
@allure.title("Оставление чекбокса выключенным")
@allure.description("Ожидание сообщения об ошибке при игнорировании обязательного чекбокса при регистрации на сайте")
def test_no_checkbox(driver):
    sign_page = SignPage(driver)
    sign_page.open()
    sign_page.enter()
    sign_page.input_mail()
    sign_page.sign()
    sign_page.error_without_checkbox()
    with allure.step("Дождаться и получить сообщение об ошибке"):
        error_message = sign_page.error_without_checkbox()

    with allure.step("Сравнить полученное сообщение с ожидаемым"):
        assert error_message == "Необходимо ваше согласие на обработку данных."


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Поиск Ж/д билетов по пути Москва — Санкт-Петербург на завтрашнюю дату")
@allure.description("Заполнение полей Откуда, Куда, Когда, получение пути следования найденных билетов")
def test_cities(driver):
    ticket_page = TicketPage(driver)
    ticket_page.open()
    ticket_page.date()
    ticket_page.input()
    way = ticket_page.check_cities()

    with allure.step("Сравнить полученное сообщение с ожидаемым"):
        assert way == "Москва — Санкт-Петербург"


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Изменение даты в информации для поиска билета")
@allure.description("Выбор другой даты для искомого билета")
def test_date_change(driver):
    search_page = SearchPage(driver)
    search_page.open()
    chosen_date = search_page.open
    search_page.change_date()
    new_date = search_page.change_date
    with allure.step("Сравнить информацию для поиска билета"):
        assert chosen_date != new_date
