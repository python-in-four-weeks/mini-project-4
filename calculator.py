import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
}


def calculate(expression: str) -> float:
    return 0


if __name__ == "__main__":
    # Try out your function here
    print(f"1 + 2 = {calculate('1 + 2')} (should be {1 + 2})")
    print(f"12 - 9 = {calculate('12 - 9')} (should be {12 - 9})")
    print(f"6 * 7 = {calculate('6 * 7')} (should be {6 * 7})")
    print(f"2 ** 6 = {calculate('2 ** 6')} (should be {2 ** 6})")
    print(f"100 / 8 = {calculate('100 / 8')} (should be {100 / 8})")
    print(f"72 // 3 = {calculate('72 // 3')} (should be {72 // 3})")
    print(f"42 % 10 = {calculate('42 % 10')} (should be {42 % 10})")
    print(f"2 * (1 + 3) = {calculate('2 * (1 + 3)')} (should be {2 * (1 + 3)})")
