# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Данные для создания заказа
order = {
    "firstName": "Дарья",
    "lastName": "Сколотина",
    "address": "Москва",
    "metroStation": 4,
    "phone": "+78003553535",
    "rentTime": 5,
    "deliveryDate": "2023-09-04",
    "comment": "Saske",
    "color": [
        "BLACK"
    ]
} 