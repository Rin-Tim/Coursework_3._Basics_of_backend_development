import os.path
from config import ROOT_DIR
from backend.utils import open_json_file, last_executed_five, data_fix, operation_from_and_to


TEST_PATH_OPERATIONS1 = os.path.join(ROOT_DIR, 'data', 'operations.json')
TEST_PATH_OPERATIONS2 = os.path.join(ROOT_DIR, 'data', 'operations_for_tests.json')
def test_open_json_file():
    assert open_json_file(TEST_PATH_OPERATIONS2) == {'test': 'test'}


def test_last_executed_five():
    assert len(last_executed_five()) == 5


def test_data_fix():
    operation1 = {'date': '2019-04-04T23:20:05.206878'}
    operation2 = {'date': '2023-05-07T18:35:29.512364'}
    assert data_fix(operation1) == "04.04.2019"
    assert data_fix(operation2) == "07.05.2023"


def test_operation_from_and_to():
    operation1 = {'from': 'Visa Gold 5999414228426353', 'to': 'Счет 90424923579946435907'}
    operation2 = {'from': 'Счет 84163357546688983493', 'to': 'Maestro 3928549031574026'}
    operation3 = {'to': 'Счет 90424923579946435907'}
    assert operation_from_and_to(operation1) == 'Visa Gold 5999 41** **** 6353 -> Счет **5907'
    assert operation_from_and_to(operation2) == 'Счет **3493 -> Maestro 3928 54** **** 4026'
    assert operation_from_and_to(operation3) == 'Отправитель не указан -> Счет **5907'
