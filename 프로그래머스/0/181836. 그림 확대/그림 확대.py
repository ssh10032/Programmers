def solution(picture, k):
    answer = []
    for i in picture:
        for _ in range(k):
            answer.append(i.replace('.', '.' * k).replace('x', 'x' * k))
    return answer