import pytest
from math import isclose

import calculator


@pytest.mark.parametrize(
    "expression",
    [
        # Single operators
        "1 + 2",
        "12 - 9",
        "6 * 7",
        "2 ** 6",
        "100 / 8",
        "72 // 3",
        "42 % 10",
        # Double operators without brackets
        "1 + 9 * 2",
        "4 ** 3 - 5",
        "12345 // 10 % 100",
        "12.5 - 50 / 8",
        # Double operators with brackets
        "(1 + 9) * 2",
        "4 ** (3 - 5)",
        "12345 // (10 % 100)",
        "(12.5 - 50) / 8",
        # Multiple operators without brackets
        "1 + 2 - 3 * 4 / 5",
        "11 ** 8 // 1000 % 10",
        # Multiple operators with brackets
        "(1 + ((2 - 3) * 4)) / 5",
        "11 ** ((1000 // 8) % 10)",
        # Signs
        "-8 - 5",
        "-20 - +23",
        "(-1 + -9) * 2",
        "-4 ** (+3 - -5)",
        "2 / -25",
        "-1000 // +12",
        "-80 % -3",
        "+11 ** ((+1000 // +8) % +10)",
        # Floats
        "1.0 + 2.0",
        "(23.45 / 5.0) - 9.87",
        "1.5 * (2.7 - 1.2)",
        "6.25 ** 3.5",
        "43.2 / 1.2",
        "83.4 // 24.6",
        "1.234 % 1.0",
        # Floats with signs
        "1.5 + -2.5",
        "-2.0 - +6.32",
        "-23.4 * 56.7",
        "+0.064 ** -1.333",
        "-1.23 / 4.56",
        "12.5 // +2.5",
        "-123.45 % -3.5",
        "-1.4 * (+2.6 ** 7)",
        # Single operators, weird spacing
        "1+2",
        " 12-9",
        "6*7 ",
        " 2**6 ",
        "100  /8",
        "72//  3",
        "42  %  10",
        # Double operators without brackets, weird spacing
        "1 +9 *2",
        " 4 **3- 5",
        "12345// 10 %100 ",
        " 12.5 -50/ 8 ",
        # Double operators with brackets, weird spacing
        "(1+9 ) *2",
        " 4** ( 3-5)",
        "12345// (10%100 ) ",
        " ( 12.5-50) /8 ",
        # Multiple operators without brackets, weird spacing
        "1 +2- 3 *4/ 5",
        "  11**  8//  1000%  10  ",
        # Multiple operators with brackets, weird spacing
        " ( 1+ ( (2-3) *4 ) ) /5 ",
        "11**((  1000//8)%10  )",
        # Signs, weird spacing
        "- 8 - 5 ",
        "- 20 -  + 23",
        "( - 1 +- 9 ) *  2",
        " - 4  ** ( +3- -5 ) ",
        "2/-25",
        "- 1000//  +12 ",
        " - 80%- 3",
        "+ 11 ** ((+ 1000 //  +8) %+ 10)",
        # Floats, weird spacing
        " 1.0+2.0",
        " (23.45/ 5.0 ) -9.87",
        "1.5*(2.7  -  1.2) ",
        " 6.25**3.5 ",
        " 43.2 /1.2",
        "83.4// 24.6 ",
        " 1.234%1.0",
        # Floats with signs, weird spacing
        "1.5+-2.5",
        "-2.0 -   -6.32",
        "- 23.4* 56.7",
        " 0.064  **  -1.333 ",
        "- 1.23/4.56",
        "12.5  //-2.5 ",
        " -123.45 %- 3.5",
        "- 1.4 * (+ 2.6 ** 7 )",
    ],
)
def test_calculator_with_valid_input(expression: str) -> None:
    expected_result = eval(expression)
    result = calculator.calculate(expression)
    assert isclose(
        result, expected_result
    ), f'Expression "{expression}" should have the result {expected_result}'


@pytest.mark.parametrize(
    "expression, expected_error_type",
    [
        ("5 / 0", ZeroDivisionError),
        ("6 // 0", ZeroDivisionError),
        ("7 % 0", ZeroDivisionError),
        ("0 ** -1", ZeroDivisionError),
        ("1234.0 ** 5678", OverflowError),
        ("4 +", SyntaxError),
        ("// 10", SyntaxError),
        ("1 + 9 2", SyntaxError),
        ("4 ** // 5", SyntaxError),
        ("12. 5 - 50 / 8", SyntaxError),
        ("1 + 9) * 2", SyntaxError),
        ("4 ** (3 - 5", SyntaxError),
        ("(12345 // (10 % 100)", SyntaxError),
        ("((12.5 - 50) / 8", SyntaxError),
        ("(1 + (2 - 3) * 4)) / 5", SyntaxError),
        ("11 ** ((1000 // 8 % 10)))", SyntaxError),
    ],
)
def test_calculator_with_invalid_input(
    expression: str, expected_error_type: type[Exception]
) -> None:
    with pytest.raises(expected_error_type) as exception:
        calculator.calculate(expression)
    assert (
        exception.type == expected_error_type
    ), f'Expression "{expression}" should generate an error of type {expected_error_type}'
