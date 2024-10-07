def solution(numbers, k):
    current_index = 0
    
    current_index = (2 * (k - 1)) % len(numbers)
    
    return numbers[current_index]