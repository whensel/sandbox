def add(numbers: str) -> int:
    # Guard clause
    if numbers == "":
        return 0

    result = 0

    if "," in numbers:
        num_list = numbers.split(",")
        for item in num_list:
            result = result + int(item)
    else:
        result = int(numbers)

    return result
