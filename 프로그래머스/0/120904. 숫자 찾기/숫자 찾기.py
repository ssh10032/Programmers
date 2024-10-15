def solution(num, k):
    n_list = list(''.join(str(num).split()))
    if str(k) in n_list:
        return n_list.index(str(k))+1
    return -1