import requests
import allure

my_headers = {
    'Content-Type': 'application/json'
    }


@allure.epic("Api")
@allure.story("Positive")
@allure.feature("POST")
@allure.severity("minor")
@allure.title("Список цен с фильтром")
@allure.description("Запрос на список цен с фильтром на нижние места в поезде, на дату 05.05.2025, от станции Сургут до станции Тюмень")
def test_list_of_prices_with_a_filter():
    base_url = "https://vid-api.tutu.ru"
    body = {
        "type": "train", "filters": ["lowerSeats"], "trips": [{"date": "05.05.2025", "from": "2030600", "to": "2030100"}], "travelers": [{"age": None}]
    }
    with allure.step("api. Выполнить POST-запрос"):
        resp = requests.post(base_url+'/api/calendar_prices', json=body, headers=my_headers)
    with allure.step("api. Проверить, что статус код равен 200"):
        assert resp.status_code == 200


@allure.epic("Api")
@allure.story("Negative")
@allure.feature("POST")
@allure.severity("minor")
@allure.title("Список цен с невалидным значением в теле запроса")
@allure.description("Запрос на список цен на дату 05.05.2025, от станции Сургут до станции Тюмень с невалидным значением для фильтра age")
def test_list_of_prices_with_an_invalid_body():
    base_url = "https://vid-api.tutu.ru"
    body = {
        "type": "train", "filters": [], "trips": [{"date": "06.01.2025", "from": "2030600", "to": "2030100"}], "travelers": [{"age": "adult"}]
    }
    with allure.step("api. Выполнить POST-запрос"):
        resp = requests.post(base_url+'/api/calendar_prices', json=body, headers=my_headers)
    with allure.step("api. Проверить, что статус код равен 400"):
        assert resp.status_code == 400
    with allure.step("api. Проверить сообщение об ошибке"):
        assert resp.json()["message"] == "Search params should have correct travelers field"


@allure.epic("Api")
@allure.story("Positive")
@allure.feature("GET")
@allure.severity("minor")
@allure.title("Список поездов для определенной станции в точную дату")
@allure.description("Запрос на список доступных поездов для станции Сургут 05.05.2025")
def test_list_of_trains_for_the_station_on_the_date():
    base_url = "https://train-gateway.tutu.ru"
    my_params = {
        'datetime': '2025-05-05T12:00:00+05:00'
        }
    with allure.step("api. Выполнить GET-запрос"):
        resp = requests.get(base_url+'/api/station/2030600/timetable?', headers=my_headers, params=my_params)
    with allure.step("api. Проверить, что статус код равен 200"):
        assert resp.status_code == 200


@allure.epic("Api")
@allure.story("Negative")
@allure.feature("GET")
@allure.severity("minor")
@allure.title("Список поездов для определенной станции с невалидной датой")
@allure.description("Запрос на список доступных поездов для станции Сургут 31.02.2025")
def test_list_of_trains_for_the_station_on_the_invalid_date():
    base_url = "https://train-gateway.tutu.ru"
    my_params = {
        'datetime': '2025-02-31T12:00:00+05:00'
        }
    with allure.step("api. Выполнить GET-запрос"):
        resp = requests.get(base_url+'/api/station/2030600/timetable?', headers=my_headers, params=my_params)
    with allure.step("api. Проверить, что статус код равен 404"):
        assert resp.status_code == 404
    with allure.step("api. Проверить сообщение об ошибке"):
        assert 'error' in resp.json()


@allure.epic("Api")
@allure.story("Positive")
@allure.feature("GET")
@allure.severity("minor")
@allure.title("Список отзывов на определенный поезд")
@allure.description("Запрос на список отзывов на поезд № 377Г")
def test_list_of_reviews_for_the_train():
    base_url = "https://www.tutu.ru"
    my_params = {
        'filter[train_number]': '377Г',
        'page[number]': '1',
        'page[size]': '5'
        }
    with allure.step("api. Выполнить GET-запрос"):
        resp = requests.get(base_url+'/train/api/v2/reviews?', headers=my_headers, params=my_params)
    with allure.step("api. Проверить, что статус код равен 200"):
        assert resp.status_code == 200
    with allure.step("api. Проверить сообщение в теле ответа"):
        assert 'data' in resp.json()


@allure.epic("Api")
@allure.story("Negative")
@allure.feature("GET")
@allure.severity("minor")
@allure.title("Список отзывов на определенный поезд с невалидными параметрами")
@allure.description("Запрос на список отзывов на поезд № 377Г без обязательных параметров")
def test_list_of_reviews_for_the_train_without_page():
    base_url = "https://www.tutu.ru"
    my_params = {
        "filter[train_number]": "377Г",
        "page[number]": "0",
        "page[size]": "0"
        }
    with allure.step("api. Выполнить GET-запрос"):
        resp = requests.get(base_url+'/train/api/v2/reviews?', headers=my_headers, params=my_params)
    with allure.step("api. Проверить, что статус код равен 400"):
        assert resp.status_code == 400
    with allure.step("api. Проверить сообщение об ошибке"):
        assert resp.json()["message"] == "The Page.number minimum is 1"
