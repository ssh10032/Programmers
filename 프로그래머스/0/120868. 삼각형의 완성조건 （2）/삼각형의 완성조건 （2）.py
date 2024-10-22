def solution(sides):
    a, b = sorted(sides)
    
    min_c = abs(a - b) + 1
    max_c = a + b - 1
    
    return max_c - min_c + 1