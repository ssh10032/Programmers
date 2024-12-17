def solution(priorities, location):
    answer = 0
    queue = [[i, priority] for i, priority in enumerate(priorities)]
    # print(queue)
    priorities.sort(reverse=True)
    # print(priorities)
    # print(priorities)
    # for i, priority in enumerate(priorities):
    #     print('index is {}'.format(i))
    #     print('priority is {}'.format(priority))
    while queue:
        idx, priority = queue[0]
        if priority == priorities[0]:
            queue.pop(0)
            priorities.pop(0)
            # print(queue)
            # print(priorities)
            answer +=1
            if idx == location:
                print('idx {} is location {}!'.format(idx, location))
                # print(i)
                # print(queue)
                # print(priorities)
                # print(answer)
                return answer
        else:
            queue.pop(0)
            queue.append([idx, priority])
            # print(priorities)
            # print(queue)
    return answer