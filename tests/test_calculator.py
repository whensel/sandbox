from string_calculator.calculator import add


def test_empty_string_returns_zero():
    result = add("")
    assert result == 0


def test_one_returns_1():
    result = add("1")
    assert result == 1


def test_add_two_numbers():
    result = add("1,2")
    assert result == 3


def test_add_three_numbers():
    result = add("1,2,3")
    assert result == 6


def test_allow_new_line():
    result = add("1\n2,3")
    assert result == 6


def test_providing_delimiter():
    result = add("//;\n1;2")
    assert result == 3
    result2 = add("//|\n1|2")
    assert result2 == 3
