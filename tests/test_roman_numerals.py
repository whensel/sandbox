from sandbox.arabicToRoman import arabicToRoman


def test_one():
    result = arabicToRoman(1)
    assert result == "I"

def test_two():
    result = arabicToRoman(2)
    assert result == "II"

def test_three():
    result = arabicToRoman(3)
    assert result == "III"

def test_four():
    result = arabicToRoman(4)
    assert result == "IV"

def test_five():
    result = arabicToRoman(5)
    assert result == "V"

def test_six():
    result = arabicToRoman(6)
    assert result == "VI"

def test_seven():
    result = arabicToRoman(7)
    assert result == "VII"

def test_eight():
    result = arabicToRoman(8)
    assert result == "VIII"

def test_nine():
    result = arabicToRoman(9)
    assert result == "IX"

def test_ten():
    result = arabicToRoman(10)
    assert result == "X"

def test_11():
    result = arabicToRoman(123)
    assert result == "CXXIII"

def test_12():
    result = arabicToRoman(999)
    assert result == "CMXCIX"

def test_13():
    result = arabicToRoman(486)
    assert result == "CDLXXXVI"

def test_14():
    result = arabicToRoman(857)
    assert result == "DCCCLVII"