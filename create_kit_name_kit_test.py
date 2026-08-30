#Сколотина Дарья 46-я когорта - Финальный проект, инженер по тестированию плюс
# Импортируем необходимые модули
import order_request
import data

# Определение функции проверки
def check_getting_order_by_track_number(order, headers):
    track_number = str(order_request.create_order(order, headers).json()["track"])
    response = order_request.get_order(track_number)

    assert response.status_code == 200

# Тест на возможность получения заказа по его номеру

def test_check_getting_order_by_track_number():
    check_getting_order_by_track_number(data.order, data.headers)
