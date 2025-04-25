import allure
import pytest
from selenium import webdriver
from SignPage import SignPage
from TicketPage import TicketPage
from SeatPage import SeatPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Регистрация на сайте через почту")
@allure.description("Проверка ввода и приянтия валидной почты для регистрации на сайте")
def test_sign(driver):
    sign_page = SignPage(driver)
    sign_page.open()
    sign_page.enter()
    sign_page.input_mail()
    sign_page.check_mail()
    mailing = sign_page.check_mail()

    with allure.step("Проверить полученное сообщение с ожидаемым"):
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
    sign_page.output_mail()
    sign_page.check_error()
    error_message = sign_page.check_error()

    with allure.step("Проверить полученное сообщение с ожидаемым"):
        assert error_message == "Без адреса электронной почты никак."


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

    with allure.step("Проверить полученное сообщение с ожидаемым"):
        assert way == "Москва — Санкт-Петербург"


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Увеличение количества пассажиров")
@allure.description("С помощью кнопки + увеличить количество взрослых пассажиров от 1 до 2, проверить изменение на странице")
def test_filter_seats(driver):
    seat_page = SeatPage(driver)
    seat_page.open()
    amount = seat_page.check_number()
    print(amount)

    with allure.step("Проверить полученный текст с ожидаемым"):
        assert amount == "Плацкарт, 2 места"


@allure.epic("UI")
@allure.story("Positive")
@allure.severity("critical")
@allure.title("Изменение стоимости билеты после отключения услуги")
@allure.description("Получение стоимости билета с услугой предоставления белья и без, проверка изменения итоговой стоимости")
def test_prices(driver):
    seat_page = SeatPage(driver)
    seat_page.open()
    seat_page.check_price()
    service = seat_page.check_price
    seat_page.check_price_without_service()
    without_service = seat_page.check_price_without_service
    with allure.step("Сравнить стоимость с услугой и без услуги"):
        assert service != without_service
