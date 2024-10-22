def solution(arr):
    arr_t = [list(x) for x in zip(*arr)]
    return 1 if arr==arr_t else 0