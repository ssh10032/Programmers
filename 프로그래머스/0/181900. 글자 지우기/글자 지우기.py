def solution(my_string, indices):
    str_list = list(my_string)
    for i in indices:
        str_list[i] = ''
    return ''.join(str_list)