import re


def add(numbers: str) -> int:
    # Guard clause
    if numbers == "":
        return 0

    string_list = create_string_list(numbers)

    return sum(map(int, string_list))


# Your function name is the documentation
def create_string_list(numbers: str) -> [str]:
    search_obj = re.match(r"//(.)\n.*", numbers, re.M | re.I)

    if search_obj:
        separator = search_obj.group(1)
        return re.sub(r"//(.)\n", "", numbers).split(separator)

    return numbers.replace("\n", ",").split(",")
