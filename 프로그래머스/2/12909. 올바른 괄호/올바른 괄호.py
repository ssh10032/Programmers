def solution(s):
    answer = True
    stack = []
    for i in s:
        # print(stack)
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if not stack:
        return True
    else:
        return False