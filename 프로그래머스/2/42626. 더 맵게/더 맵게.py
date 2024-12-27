import heapq
def solution(scoville, K):
    # print('Non-heap list is {}'.format(scoville))
    heapq.heapify(scoville)
    # print('heapify list is {}'.format(scoville))
    try_num = 0
    new_v = 0
    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        v1 = heapq.heappop(scoville)
        v2 = heapq.heappop(scoville)
        new_v = v1 + v2 * 2
        try_num+=1
        heapq.heappush(scoville, new_v)            
    return try_num