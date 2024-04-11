import json
import datetime


def open_json_file(file_path):
    """Чтение файла JSON"""
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        return data


def last_executed_five():
    """Сортирует и выводит последние 5 операций на экран"""
    file_path = '../data/operations.json'  # Путь к файлу json
    operation_data = open_json_file(file_path)

    list_executed = []

    # Фильтрация по статусу 'EXECUTED'
    for e in operation_data:
        if e.get('state') == 'EXECUTED':
            list_executed.append(e)

    # Сортировка и вывод последних 5 операций
    last_list = sorted(list_executed, key=lambda x: x['date'], reverse=True)
    five_op = last_list[:5]

    return five_op


def data_fix(date_):
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)"""

    date_formate = date_['date']
    the_date = datetime.datetime.strptime(date_formate, '%Y-%m-%dT%H:%M:%S.%f')
    th_date = the_date.strftime('%d.%m.%Y')
    return th_date


def operation_from_and_to(operation):
    """Маскирование карты или счёта"""
    operation_from = operation.get('from')
    operation_to = operation.get('to')

    if operation_from:
        parts = operation_from.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            hidden_number = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            operation_from = f"{" ".join(parts[:-1])} {hidden_number}"
        else:
            operation_from = f'Счет **{numbers[-4:]}'

    if operation_to:
        parts = operation_to.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            hidden_number = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            operation_to = f"{" ".join(parts[:-1])} {hidden_number}"
        else:
            operation_to = f'Счет **{numbers[-4:]}'

    if operation_from == None:
        operation_from = 'Отправитель не указан'

    return f"{operation_from} -> {operation_to}"
