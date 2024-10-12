def solution(myString):
    list = ' '.join(myString.split("x")).split()
    list.sort()
    return list