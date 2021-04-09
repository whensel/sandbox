def add(numbers: str) -> int:
    # Guard clause
    if numbers == "":
        return 0

    return sum(map(int, numbers.split(",")))