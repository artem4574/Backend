import subprocess
import pytest

INTERPRETER = 'python'


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
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6', 'Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['-6', '3'], ['-3', '-9', '-18']),
        (['0', '9'], ['9', '-9', '0'])
    ],
    'anagram': [
        (['backend', 'bandeck'], 'YES'),
        (['hfejnt', 'hfejntttt'], 'NO'),
        (['operation', 'Operation'], 'NO'),
        (['price', 'price'], 'YES'),
        (['123456789', '987654321'], 'YES')
    ],
    'division': [
        (['10', '3'], ['3', '3.3333333333333335']),
        (['2', '1'], ['2', '2.0']),
        (['8', '0'], ['Type error: division by 0.'])
    ],
    'loops': [
        ('5', ['0', '1', '4', '9', '16']),
        ('10', ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81']),
        ('1', ['0']),
        ('8', ['0', '1', '4', '9', '16', '25', '36', '49'])
    ],
    'print_function': [
        ('5', ['12345']),
        ('8', ['12345678']),
        ('1', ['1']),
        ('0', '')
    ],
    'second_score': [
        (['5', '2 3 6 6 5'], '5'),
        (['8', '1 10 51 99 99 99 98 99'], '98'),
        (['6', '-1 -5 0 5 -1 -100'], '0')
    ],
    'lists': [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], '[1, 3, 2]'),
        (['6', 'insert 0 5', 'append 3', 'append 4', 'reverse', 'pop', 'print'], '[4, 3]'),
        (['3', 'append 1', 'remove 1', 'print'], '[]')
    ],
    'nested_list': [
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], ['Харш']),
        (['4', 'Max', '37.21', 'John', '37.21', 'Steve', '37.2', 'Amy', '41'], ['John', 'Max']),
        (['2', 'Garry', '40', 'Kenny', '41'], ['Garry'])
    ],
    'swap_case': [
        ('Hello World', 'hELLO wORLD'),
        ('PyThOn', 'pYtHoN'),
        ('12345', '12345'),
        ('Привет, Мир!', 'пРИВЕТ, мИР!')
    ],
    'split_and_join': [
        ('Hello World', 'Hello-World'),
        ('Python is awesome', 'Python-is-awesome'),
        ('12345', '12345'),
        ('0 00 0 0 000', '0-00-0-0-000')
    ],
    'metro': [
        (['8', '1 5', '6 10', '11 15', '8 22', '3 4', '1 30', '8 66', '4 9', '8'], '5'),
        (['3', '1 5', '6 10', '2 4', '4'], '2'),
        (['4', '1 5', '6 10', '11 15', '16 20', '7'], '1'),
        (['2', '2 3', '6 10', '4'], '0')
    ],
    'minion_game': [
        ('BANANA', 'Стюарт 12'),
        ('APPLE', 'Стюарт 9'),
        ('BANANAS', 'Стюарт 16'),
        ('THEME', 'Стюарт 11')
    ],
    'is_leap': [
        ('2000', 'True'),
        ('2020', 'True'),
        ('1900', 'False'),
        ('2047', 'False'),
        ('2048', 'True')
    ],
    'happiness': [
        (['3 2', '1 5 3', '3 1', '5 7'], '1'),
        (['4 3', '1 2 3 4', '5 1 4', '3 4 8'], '0'),
        (['5 4', '1 2 3 4 5', '3 4 7 6', '5 4 3 2 0'], '-2')
    ],
    'pirate_ship': [
        (['45 4', 'ром 100 200', 'алмазы 2 2000', 'мука 150 400', 'сабли 10 1000'],
         ['алмазы 2 2000.0', 'сабли 10 1000.0', 'мука 33 88.0']),
        (['500 7', 'крабы 10 500', 'уголь 500 750', 'брилианты 8 10000', 'сапоги 70 1400', 'пистолеты 90 3600',
          'вода 500 1000', 'грибы 2 7500'],
         ['грибы 2 7500.0', 'брилианты 8 10000.0', 'крабы 10 500.0', 'пистолеты 90 3600.0', 'сапоги 70 1400.0',
          'вода 320 640.0'])
    ],
    'matrix_mult': [
        (['2', '1', '2', '3', '4', '3', '2', '3', '5'], ['[9, 12]', '[21, 26]']),
        (['3', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '8', '7', '6', '5', '4', '3', '2', '1'],
         ['[30, 24, 18]', '[84, 69, 54]', '[138, 114, 90]']),
        (['2', '7', '4', '3', '5', '23', '5', '7', '9'], ['[189, 71]', '[104, 60]']),
        (['2', '5', '33', '0', '9', '28', '45', '75', '69'], ['[2615, 2502]', '[675, 621]'])
    ]
}


def test_hello_world():
    assert run_script('hw_1/source/hello.py') == 'Hello, World!'


@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('hw_1/source/python_if_else.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('hw_1/source/arithmetic_operators.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('hw_1/source/anagram.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('hw_1/source/division.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('hw_1/source/loops.py', [input_data]) == '\n'.join(expected)


@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('hw_1/source/print_function.py', [input_data]) == '\n'.join(expected)


@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('hw_1/source/second_score.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_lists(input_data, expected):
    assert run_script('hw_1/source/nested_list.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('hw_1/source/swap_case.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('hw_1/source/split_and_join.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('hw_1/source/metro.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('hw_1/source/minion_game.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('hw_1/source/is_leap.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('hw_1/source/happiness.py', input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('hw_1/source/pirate_ship.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('hw_1/source/matrix_mult.py', input_data).split('\n') == expected
