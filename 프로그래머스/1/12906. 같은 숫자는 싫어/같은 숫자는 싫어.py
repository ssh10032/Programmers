def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[0])
        else:
            if answer[-1] == arr[i]:
                pass
            else:
                answer.append(arr[i])
    # print(answer)
    return answer