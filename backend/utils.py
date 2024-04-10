import json
import datetime


def open_json_file(file_path):
    """Чтение файла JSON"""
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        return data


def last_executed_five(operation_data):
    """Выводит последние 5 операций на экран"""
    list_executed = []

    for e in operation_data:
        if e.get('state') == 'EXECUTED':
            list_executed.append(e)

    last_list = sorted(list_executed, key=lambda x: x['date'], reverse=True)

    return last_list


def data_fix(date_):
    date_formate = date_['date']
    the_date = datetime.datetime.strptime(date_formate, '%Y-%m-%dT%H:%M:%S.%f')
    th_date = the_date.strftime('%d.%m.%Y')
    return th_date

а = [1, 2, 3, 4, 5]
print(len(a))


if c.get('from') in 'карта'

# file_path = '../data/operations.json'
# json_data = open_json_file(file_path)
# a = last_executed_five(json_data)[:5]
# for i in a:
#     print(data_fix(i))


# file_path = '../data/operations.json'
# json_data = open_json_file(file_path)
# print(json_data)
