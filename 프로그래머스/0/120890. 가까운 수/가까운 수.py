def solution(array, n):
    min_value = min([abs(i-n) for i in array])
    v_list = [v for i, v in enumerate(array) if abs(v-n)==min_value]
    return min(v_list)