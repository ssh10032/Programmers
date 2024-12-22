def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and stack[-1][1] > prices[i]:
            idx, price = stack.pop()
            answer[idx] = i-idx
        stack.append((i, prices[i]))
    print(stack)
    while stack:
        idx, price = stack.pop()
        answer[idx] = n - 1 - idx
        
    return answer