def solution(numbers):
    if len(numbers)==2:
        return numbers[0] * numbers[1]
    minus_list = [abs(i) for i in numbers if i <0]
    plust_list = [i for i in numbers if i >0]
    minus_list.sort()
    plust_list.sort()
    if len(minus_list)>1:
        m_max = minus_list[-2] * minus_list[-1]
    else:
        m_max = 0
        
    if len(plust_list)>1:
        p_max = plust_list[-2] * plust_list[-1]
    else:
        p_max = 0
    
    return p_max if p_max>m_max else m_max