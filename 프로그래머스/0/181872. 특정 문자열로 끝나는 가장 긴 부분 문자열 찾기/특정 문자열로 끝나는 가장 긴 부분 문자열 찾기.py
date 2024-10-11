def solution(myString, pat):
    idx = myString.rfind(pat)
    length = len(pat)
    return myString[:idx+length]