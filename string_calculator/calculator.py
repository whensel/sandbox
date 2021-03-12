def add(numbers: str) -> int:
    if numbers == "":
        return 0

    if "," in numbers:
        [x, y] = numbers.split(",")
        result = int(x) + int(y)
    else:
        result = int(numbers)

    return result
