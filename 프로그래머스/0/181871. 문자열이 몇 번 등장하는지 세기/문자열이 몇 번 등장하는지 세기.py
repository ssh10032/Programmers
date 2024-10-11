def solution(myString, pat):
    count = 0
    start = 0
    
    while start <= len(myString) - len(pat):
        if myString[start:start+len(pat)] == pat:
            count += 1
        start += 1
    
    return count