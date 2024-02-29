import subprocess
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath('C:/Users/nrvn2/PycharmProjects/Backend/hw_2/source'))

INTERPRETER = 'python3'
PROGRAM_FILENAME = 'my_sum_argv.py'


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


def run_program(*args):
    proc = subprocess.run(
        [INTERPRETER, PROGRAM_FILENAME, *args],
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


fact_test_data = {
    'fact': [
        (5, 120),
        (6, 720),
        (0, 1),
        (20, 2432902008176640000)
    ]
}

fibonacci_test_data = {
    'fibonacci': [
        (5, [0, 1, 1, 8, 27]),
        (8, [0, 1, 1, 8, 27, 125, 512, 2197]),
        (0, [0]),
        (10, [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304])
    ]
}

summer_test_data = {
    'summer': [
        ([1, 2, 3, 4, 5, 88767], 88782),
        ([], 0),
        ([10, -5, 3], 8),
    ]
}

show_employee_test_data = {
    'show_employee': [
        (("Иванов Петр Иванович",), "Иванов Петр Иванович: 100000 ₽"),
        (("Сидоров Андрей", 120000), "Сидоров Андрей: 120000 ₽"),
        (("Анна", 95000), "Анна: 95000 ₽")
    ]
}

sum_and_sub_test_data = {
    'sum_and_sub': [
        ([0, 0], (0, 0)),
        ([100, 99], (199, 1)),
        ([5, 240], (245, -235))
    ]
}

process_list_test_data = {
    'process_list': [
        ([range(20)], [0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859]),
        ([range(1)], [0]),
        ([range(7)], [0, 1, 4, 27, 16, 125, 36])
    ]
}

email_val_test_data = {
    'email_validation': [
        ([['lara@mospolytech.ru', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.russ']],
         ['brian-23@mospolytech.ru', 'lara@mospolytech.ru']),
        ([['lara@mospolytech.', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.russ']], ['brian-23@mospolytech.ru']),
        ([['lara@mospolytech.', 'briaн-23@mospolytech.ru', 'britts_54@mospolytech.russ']], [])
    ]
}

my_sum_argv_test_data = [
    ('python3 hw_2\source\my_sum_argv.py 1 2 3 4 5', '15.0')
]


@pytest.mark.parametrize("input_data, expected", fact_test_data['fact'])
def test_fact_it(input_data, expected):
    from ..source.fact import fact_it
    assert fact_it(input_data) == expected


@pytest.mark.parametrize("input_data, expected", fibonacci_test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    from ..source.fibonacci import fibonacci
    assert fibonacci(input_data) == expected


@pytest.mark.parametrize("input_data, expected", summer_test_data['summer'])
def test_summer(input_data, expected):
    from ..source.my_sum import summer
    assert summer(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", show_employee_test_data['show_employee'])
def test_show_employee(input_data, expected):
    from ..source.show_employee import show_employee
    assert show_employee(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", sum_and_sub_test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    from ..source.sum_and_sub import sum_and_sub
    assert sum_and_sub(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", process_list_test_data['process_list'])
def test_process_list(input_data, expected):
    from ..source.process_list import process_list
    assert process_list(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", email_val_test_data['email_validation'])
def test_email_validation(input_data, expected):
    from ..source.email_validation import filter_mail
    assert filter_mail(*input_data) == expected


@pytest.mark.parametrize("input_params, expected_output", my_sum_argv_test_data)
def test_my_sum_argv(input_params, expected_output):
    output = run_program(*input_params)
    assert output == expected_output
