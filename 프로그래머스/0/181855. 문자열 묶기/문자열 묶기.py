def solution(strArr):
    len_strArr = [len(i) for i in strArr]
    u_len = []
    for i in len_strArr:
        if i not in u_len:
            u_len.append(i)
    return max(len_strArr.count(i) for i in u_len) 