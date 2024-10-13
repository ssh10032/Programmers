def solution(numbers):
    for index, value in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                                   numbers = numbers.replace(value, str(index))
    return int(numbers)