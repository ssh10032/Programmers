def solution(s):
    stack = []
    for i in s:
        # print(stack)
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return not stack