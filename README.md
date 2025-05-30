# project5
## Project5 - это проект для обработки и фильтрации банковских операций. 
## Приложение позволяет фильтровать операции по статусу и сортировать их по дате.
## Установка
1. Клонируйте репозиторий:
```
git clone https://github.com/Liikas/project5/tree/feature/homework_10_1
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
1. Импортируете модуль processing(import processing)
2. Вызываете функции filter_by_state и sort_by_date
3. Пример ввода данных для filter_by_state: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
4. Пример ввода данных для sort_by_date: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

## Докуметация 
Функция filter_by_state принимает список словарей и опционально значение для ключа 
state(по умолчанию'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.
Функция sort_by_date принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
Функция должна возвращать новый список, отсортированный по дате (date).
Функция filter_by_currency принимает список транзакций и нужную вам валюту, после чего
возвращает список транзакций только с нужной вам валютой.
Функция transaction_descriptions принимает на вход список тразакций и возвращает описания 
транзакций. 
Функция card_number_generator начало и конец для генерации уникального номера карты.
card_number_generator возвращает на выход номер карты учитывая данный вами диапазоном


## Тестирование 
Для тестирования функций был использован pytest. 
Были протестированы различные сценарии функций, такие как некорректное количество цифр в номере карты или же в номере счета,
неправильное название карты или счета, неверная сортировка данных по дате или же статусу и т.д.
Также были протестированы такие сценарии как отрицательный диапазон, пустой список,
отсутствие валюты и т.д.
Были учтены как позитивные так и негативные сценарии. Также в данном проекте были использованы такие методы тестирования 
как параметризация и фикстуры.



## Лицензия
Этот проект лицензирован по [ лицензии Apache License 2.0](LICENSE).
