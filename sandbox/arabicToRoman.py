from functools import reduce


conversion_rules = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def highest_reducer(number, converters):
    return next(filter(lambda y: y <= number, converters))


def arabic_to_roman(number):
    def inner(number, reduced_value=""):
        if number == 0:
            return reduced_value

        hr = highest_reducer(number, list(conversion_rules.keys())[::-1])
        return inner(number - hr, reduced_value + conversion_rules[hr])

    result = inner(number)
    return result
