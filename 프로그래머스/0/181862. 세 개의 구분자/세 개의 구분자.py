def solution(myStr):
    split_list = ['a', 'b', 'c']
    c_list = myStr
    for i in split_list:
        c_list = ' '.join(c_list.split(i))
    c_list = c_list.split()
    
    return c_list if len(c_list)>0 else ["EMPTY"]