def solution(myString):
    return ''.join([i if ord(i)>108 else 'l' for i in myString ])