def solution(s):
    unique_str = list(set(s))
    unique_str.sort()
    answer = ''
    for i in unique_str:
        if s.count(i)==1:
            answer+=i
    return answer