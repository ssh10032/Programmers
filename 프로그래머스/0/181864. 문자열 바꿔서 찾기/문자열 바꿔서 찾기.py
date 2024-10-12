def solution(myString, pat):
    dic = {"A" : "B", "B" : "A"}
    c_String = ''.join([dic[i] for i in myString])
    return 1 if pat in c_String else 0