from sandbox.arabicToRoman import arabic_to_roman


def test_one():
    result = arabic_to_roman(1)
    assert result == "I"


def test_two():
    result = arabic_to_roman(2)
    assert result == "II"


def test_three():
    result = arabic_to_roman(3)
    assert result == "III"


def test_four():
    result = arabic_to_roman(4)
    assert result == "IV"


def test_five():
    result = arabic_to_roman(5)
    assert result == "V"


def test_six():
    result = arabic_to_roman(6)
    assert result == "VI"


def test_seven():
    result = arabic_to_roman(7)
    assert result == "VII"


def test_eight():
    result = arabic_to_roman(8)
    assert result == "VIII"


def test_nine():
    result = arabic_to_roman(9)
    assert result == "IX"


def test_ten():
    result = arabic_to_roman(10)
    assert result == "X"


def test_11():
    result = arabic_to_roman(123)
    assert result == "CXXIII"


def test_12():
    result = arabic_to_roman(999)
    assert result == "CMXCIX"


def test_13():
    result = arabic_to_roman(486)
    assert result == "CDLXXXVI"


def test_14():
    result = arabic_to_roman(857)
    assert result == "DCCCLVII"
