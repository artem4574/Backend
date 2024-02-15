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

