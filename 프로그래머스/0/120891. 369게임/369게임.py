def solution(order):
    n_list = str(order)
    count = 0
    for i in n_list:
        if i in ["3", "6", "9"]:
            count+=1
    return count