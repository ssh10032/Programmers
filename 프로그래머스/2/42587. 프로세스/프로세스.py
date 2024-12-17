def solution(priorities, location):
    answer = 0
    queue = [[i, priority] for i, priority in enumerate(priorities)]
    priorities.sort(reverse=True)
    while True:
        idx, priority = queue[0]
        if priority == priorities[0]:
            queue.pop(0)
            priorities.pop(0)
            answer +=1
            if idx == location:
                return answer
        else:
            queue.pop(0)
            queue.append([idx, priority])
    return answer