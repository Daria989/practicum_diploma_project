# Импортируем модуль configuration
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

#Импортируем модуль data с данными о заказе
import data

#Определение функции POST-запроса на создание заказа
def create_order(order_body, new_headers):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=new_headers, json=order_body)

# Определение функции на получение заказа по номеру
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track)




