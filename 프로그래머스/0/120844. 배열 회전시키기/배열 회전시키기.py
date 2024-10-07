def solution(numbers, direction):
    answer = []
    if direction =="right":
        a=numbers[-1]
        answer.append(a)
        for i in range(len(numbers)-1):
            answer.append(numbers[i])
    else:
        a=numbers[0]
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(a)
    return answer