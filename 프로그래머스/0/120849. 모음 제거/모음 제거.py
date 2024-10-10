def solution(my_string):
    r_list = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i in r_list:
            my_string = my_string.replace(i, '')
    return my_string