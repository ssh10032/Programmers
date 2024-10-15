def solution(num_str):
    n_list = list(''.join(num_str.split()))
    answer = 0
    for i in n_list:
        answer+=int(i)
    return answer