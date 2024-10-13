def solution(arr, k):
    # u_arr = list(set(arr))
    u_arr = []
    for i in arr:
        if i not in u_arr:
            u_arr.append(i)
    if len(u_arr)>=k:
        return u_arr[:k]
    else:
        return u_arr + [-1] * (k-len(u_arr))