import subprocess
from pathlib import Path


def test_pipe_once():
    # GIVEN
    # An imported Pipe instance and a certain input.
    from src.simple_pipe import Pipe

    input_ = (1, 2, 3)

    # WHEN
    # The Pipe instance is defined and used.
    function = Pipe | list | reversed | iter | next
    result = function(input_)

    # THEN
    # The result is the same as applying the functions in order.
    assert next(iter(reversed(list(input_)))) == result == 3


def test_pipe_multiple_times():
    # GIVEN
    # An imported Pipe instance and two inputs.
    from src.simple_pipe import Pipe

    input_A = (1, 2, 3)
    input_B = ["sasquatch"]

    # WHEN
    # The Pipe instance is defined and used twice for different functions.
    function_A = Pipe | list | reversed | iter | next
    result_A = function_A(input_A)

    function_B = Pipe | iter | next | len
    result_B = function_B(input_B)

    # THEN
    # The results are both the same as applying the functions in order.
    assert next(iter(reversed(list(input_A)))) == result_A == 3

    assert len(next(iter(input_B))) == result_B == 9


def test_correctly_typed_code():
    # GIVEN
    # A code file where Pipe gets correctly typed functions.
    python_file = Path("tests/code_with_correct_types.py")

    # WHEN
    # this code file is type checked with pyright.
    result = subprocess.run(["pyright", python_file], capture_output=True, text=True)

    # THEN
    # pyright detects no issues.
    assert result.returncode == 0
    assert "0 errors" in result.stdout


def test_wrongly_typed_code(tmpdir):
    # GIVEN
    # A piece of code where Pipe gets wrongly typed functions
    code = """
from src.simple_pipe import Pipe

function_with_incorrect_type = Pipe | list | next
"""
    python_file = tmpdir / "incorrect.py"

    with python_file.open("w") as f:
        f.write(code)

    # WHEN
    # this code file is type checked with pyright
    result = subprocess.run(["pyright", python_file], capture_output=True, text=True)

    # THEN
    # pyright detects that the pipe gets constructed with wrongly typed functions
    assert result.returncode == 1
    assert "reportOperatorIssue" in result.stdout


def test_quad():
    from src.simple_pipe import Pipe, partial2
    from itertools import count, islice

    first_ten_quad = (
        Pipe | count | partial2(map, lambda x: x**2) | partial2(islice, arg2=10) | sum
    )
    assert first_ten_quad(0) == 285


def test_pipe_with_strings():
    from src.simple_pipe import Pipe

    # Test string processing pipeline
    process_string = Pipe | str.upper | str.strip | (lambda x: x.replace(" ", "_"))
    assert process_string("  hello world  ") == "HELLO_WORLD"


def test_pipe_with_math():
    from src.simple_pipe import Pipe, partial2
    import math

    # Test mathematical pipeline
    calc = Pipe | abs | math.sqrt | partial2(round, arg2=2)
    assert calc(-16) == 4.0


def test_pipe_with_collections():
    from src.simple_pipe import Pipe, partial2
    from collections import Counter

    # Test pipeline with collections and filtering
    word_frequency = (
        Pipe | str.lower | str.split | partial2(filter, lambda x: len(x) > 3) | Counter
    )

    result = word_frequency("The quick brown fox jumps over lazy dogs")
    assert result["quick"] == 1
    assert result["brown"] == 1
    assert len(result) == 6  # Words longer than 3 letters


def test_pipe_composition():
    from src.simple_pipe import Pipe

    # Test composing multiple pipes
    transform1 = Pipe | str.upper | str.strip
    transform2 = Pipe | (lambda x: x.replace(" ", "-"))

    # Combine transformations using pipe composition
    combined = Pipe | transform1 | transform2

    assert combined("  hello world  ") == "HELLO-WORLD"
