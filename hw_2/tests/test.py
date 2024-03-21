import subprocess
import sys
import pytest
import os
from ..source.plane_angle import Point
from ..source.complex_numbers import Complex


INTERPRETER = 'python3'
sys.path.insert(0, os.path.abspath('C:/Users/nrvn2/PycharmProjects/Backend/hw_2/source'))


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'fact': [
        (5, 120),
        (6, 720),
        (0, 1),
        (15, 1307674368000),
        (20, 2432902008176640000)
    ],
    'fibonacci': [
        (5, [0, 1, 1, 8, 27]),
        (8, [0, 1, 1, 8, 27, 125, 512, 2197]),
        (0, [0]),
        (10, [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304])
    ],
    'summer': [
        ([1, 2, 3, 4, 5, 88767], 88782),
        ([], 0),
        ([10, -5, 3], 8),
        ([10, 10, 10], 30)
    ],
    'my_sum_argv': [
        ([1, 3, 5, 7, 9], 25),
        ([2, 4, 6, 8], 20),
        ([7, 3, 41], 51),
        ([32, 171], 203),
        ([-100, 200, 600, -400], 300)
    ],
    'show_employee': [
        (("Иванов Петр Иванович",), "Иванов Петр Иванович: 100000 ₽"),
        (("Сидоров Андрей", 120000), "Сидоров Андрей: 120000 ₽"),
        (("Анна", 95000), "Анна: 95000 ₽"),
        (("Петров Иван Алексеевич",), "Петров Иван Алексеевич: 100000 ₽")
    ],
    'sum_and_sub': [
        ([0, 0], (0, 0)),
        ([100, 99], (199, 1)),
        ([3, 3], (6, 0)),
        ([5, 240], (245, -235)),
        ([1, 1], (2, 0))
    ],
    'process_list': [
        ([range(20)], [0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859]),
        ([range(1)], [0]),
        ([range(2)], [0, 1]),
        ([range(7)], [0, 1, 4, 27, 16, 125, 36])
    ],
    'email_validation': [
        ([['lara@mospolytech.ru', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.russ']],
         ['brian-23@mospolytech.ru', 'lara@mospolytech.ru']),
        ([['lara@mospolytech.', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.russ']], ['brian-23@mospolytech.ru']),
        ([['lara@mospolytech.', 'briaн-23@mospolytech.ru', 'britts_54@mospolytech.russ']], [])
    ],
    'files_sort': [
        (os.getcwd(), ['.gitignore', 'README.md'])
    ],
    'file_search': [
        ('__init__.py', True),
        ('fact.py', False),
        ('1.txt', False),
        ('a.txt', False),
        ('b.txt', False)
    ],
    'average_scores': [
        ([(89.0, 90.0, 78.0, 93.0, 80.0), (90.0, 91.0, 85.0, 88.0, 86.0), (91.0, 92.0, 83.0, 89.0, 90.5)],
         (90.0, 91.0, 82.0, 90.0, 85.5)),
        ([(10, 20, 30), (30, 10, 20), (40, 30, 20), (10, 10, 10), (30, 20, 40)], (24.0, 18.0, 24.0)),
        ([(5, 10), (7, 12)], (6.0, 11.0)),
        ([(0, 6), (3, 0)], (1.5, 3.0))
    ],
    'plane_angle': [
        ([Point(0, 7, 1), Point(2, -1, 5), Point(1, 6, 3), Point(3, -9, 8)], 140.76847951640775),
        ([Point(1, 2, 0), Point(2, 2, 0), Point(2, 3, 0), Point(3, 3, 0)], 180.0),
        ([Point(6, 3, 0), Point(12, 78, 0), Point(2, 3, 10), Point(0, 5, 7)], 61.19649343422453),
        ([Point(67, 0, 4), Point(1, 6, 34), Point(2, 3, 90), Point(4, 5, 76)], 35.52562731540138)

    ],
    'sort_phone': [
        (['09035434606', '89258878675', '9195969878'], ['+7 (903) 543-46-06', '+7 (919) 596-98-78', '+7 (925) 887-86-75']),
        (['7856409816', '6745368907', '87810674537'], ['+7 (674) 536-89-07', '+7 (781) 067-45-37', '+7 (785) 640-98-16']),
        (['05643189509', '06734256410'], ['+7 (564) 318-95-09', '+7 (673) 425-64-10']),
    ],
    'name_format': [
        ([['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']],
         ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
        ([['Artem', 'Savrasov', '20', 'M'], ['Alex', 'Smith', '19', 'M'], ['Ada', 'Stevenson', '18', 'F']],
         ['Ms. Ada Stevenson', 'Mr. Alex Smith', 'Mr. Artem Savrasov'])
    ],
    'comp_operate': [
        ([Complex(2, 1), Complex(5, 6)],
         ['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']),
        ([Complex(7, 2), Complex(3, 4)],
         ['10.00+6.00i', '4.00-2.00i', '13.00+34.00i', '1.16-0.88i', '7.28+0.00i', '5.00+0.00i']),
        ([Complex(1, 2), Complex(9, 0)],
         ['10.00+2.00i', '-8.00+2.00i', '9.00+18.00i', '0.11+0.22i', '2.24+0.00i', '9.00+0.00i'])
    ],
    'circle_square_mk': [
        ([5, 10000000], 78),
        ([8, 1400000], 201),
        ([4.5, 150000], 63),
        ([2, 3000000], 12)
    ]
}


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    from ..source.fact import fact_it
    assert fact_it(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    from ..source.fibonacci import fibonacci
    assert fibonacci(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['summer'])
def test_summer(input_data, expected):
    from ..source.my_sum import summer
    assert summer(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    from ..source.my_sum_argv import summer
    assert summer(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    from ..source.show_employee import show_employee
    assert show_employee(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    from ..source.sum_and_sub import sum_and_sub
    assert sum_and_sub(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    from ..source.process_list import process_list
    assert process_list(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    from ..source.email_validation import filter_mail
    assert filter_mail(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    from ..source.files_sort import list_files
    assert list_files(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    from ..source.file_search import search_file_recursive
    assert search_file_recursive(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['average_scores'])
def test_average_scores(input_data, expected):
    from ..source.average_scores import av_score
    assert av_score(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    from ..source.plane_angle import plane_angle
    assert plane_angle(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['sort_phone'])
def test_sort_phone(input_data, expected):
    from ..source.phone_number import sort_phone
    assert sort_phone(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['name_format'])
def test_name_format(input_data, expected):
    from ..source.people_sort import name_format
    assert name_format(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['comp_operate'])
def test_complex_actions(input_data, expected):
    from ..source.complex_numbers import comp_operate
    assert comp_operate(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['circle_square_mk'])
def test_circle_square_mk(input_data, expected):
    from ..source.circle_square_mk import circle_square_mk
    assert circle_square_mk(*input_data) == expected
