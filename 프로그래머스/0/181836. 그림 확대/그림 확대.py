def solution(picture, k):
    answer = []
    for i in picture:
        s_str = ''
        for j in i:
            s_str+=j*k
        for n in range(k):
            answer.append(s_str)
    return answer