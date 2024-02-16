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
        (['10', '5'], ['15', '5', '50'])
    ],
    'anagram': [
        (['backend', 'bandeck'], 'YES'),
        (['hfejnt', 'hfejntttt'], 'NO'),
        (['operation', 'Operation'], 'NO'),
    ],
    'division': [
        (['10', '3'], ['3', '3.3333333333333335']),
        (['2', '1'], ['2', '2.0']),
        (['8', '0'], ['Type error: division by 0.'])
    ],
    'loops': [
        ('5', ['0', '1', '4', '9', '16']),
        ('10', ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81'])
    ],
    'print_function': [
        ('5', ['12345']),
        ('8', ['12345678'])
    ],
    'second_score': [
        (['5', '2 3 6 6 5'], '5'),
        (['8', '1 10 51 99 99 99 98 99'], '98')
    ],
    'lists': [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], '[1, 3, 2]')
    ],
    'nested_list': [
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], 'Харш')
    ],
    'swap_case': [
        ('Hello World', 'hELLO wORLD'),
        ('PyThOn', 'pYtHoN'),
        ('12345', '12345')
    ],
    'split_and_join': [
        ('Hello World', 'Hello-World'),
        ('Python is awesome', 'Python-is-awesome'),
        ('12345', '12345')
    ],
    'metro': [
        (['8', '1 5', '6 10', '11 15', '8 22', '3 4', '1 30', '8 66', '4 9', '8'], '5'),
        (['3', '1 5', '6 10', '2 4', '4'], '2'),
        (['4', '1 5', '6 10', '11 15', '16 20', '7'], '1')
    ],
    'minion_game': [
        ('BANANA', 'Стюарт 12'),
        ('APPLE', 'Стюарт 9'),
        ('BANANAS', 'Стюарт 16')
    ],
    'is_leap': [
        ('2000', 'True'),
        ('2020', 'True'),
        ('1900', 'False')
    ],
    'happiness': [
        (['3 2', '1 5 3', 'a b'], '1'),
        (['4 3', '1 2 3 4', 'a b c'], '0'),
        (['5 4', '1 2 3 4 5', 'a b c d'], '-2')
    ],
    'pirate_ship': [
        (['3 50', 'gold 60 10', 'silver 100 20', 'diamond 120 30'], ['[2 20 40.00]', '[1 30 40.00]']),
        (['4 100', 'gold 50 10', 'silver 100 20', 'diamond 200 30', 'platinum 150 40'], ['[3 30 60.00]', '[2 40 80.00]', '[1 30 30.00]']),
        (['2 10', 'gold 20 5', 'silver 30 8'], '1 5 10.00')
    ],
    'matrix_mult': [
        (['2', '1', '2', '3', '4', '3', '2', '3', '5'], ['[7, 10]', '[15, 22]']),
        (['3', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '8', '7', '6', '5', '4', '3', '2', '1'], ['[30, 36, 42]', '[66, 81, 96]', '[102, 126, 150]'])
    ]
}


def test_hello_world():
    assert run_script('source/hello.py') == 'Hello, World!'


@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('source/python_if_else.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('source/arithmetic_operators.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('source/anagram.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('source/division.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('source/loops.py', [input_data]) == '\n'.join(expected)


@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('source/print_function.py', [input_data]) == '\n'.join(expected)


@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('source/second_score.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_lists(input_data, expected):
    assert run_script('source/nested_list.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('source/swap_case.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('source/split_and_join.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('source/metro.py', input_data).split('\n') == [expected]


@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('source/minion_game.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_swap_case(input_data, expected):
    assert run_script('source/is_leap.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_swap_case(input_data, expected):
    assert run_script('source/happiness.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_swap_case(input_data, expected):
    assert run_script('source/pirate_ship.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_swap_case(input_data, expected):
    assert run_script('source/matrix_mult.py', input_data).split('\n') == expected
