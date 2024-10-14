def solution(my_string):
    str_list = my_string.split()
    v = int(str_list[0])
    for i in range(1, len(str_list),2):
        op = str_list[i]
        if op == '+':
            v += int(str_list[i+1])
        else:
            v -= int(str_list[i+1])
    return v