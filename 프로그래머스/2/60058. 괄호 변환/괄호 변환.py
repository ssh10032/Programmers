
def check_balance(target_str):
    if target_str[0]!='(':
        return False

    stack_list = []
    for i in range(len(target_str)):
        if target_str[i] == '(':
            stack_list.append('')
        else:
            if len(stack_list)==0:
                return False
            else:
                stack_list.pop()
    return len(stack_list)==0

def spr_str(target_str):
    stk_str = target_str[0]
    stack_list = []
    u_idx = 0
    for i in range(len(target_str)):
        if target_str[i] == stk_str:
            if i!=0 and len(stack_list)==0:
                u_idx = i
                break
            stack_list.append('')
        else:
            if len(stack_list)==0:
                u_idx = i
                break
            else:
                stack_list.pop()
                if len(stack_list)==0:
                    u_idx = i
                    break
    return target_str[:u_idx+1], target_str[u_idx+1:]

def dfs(str_list):
    if len(str_list) == 0:
        return ''
    u, v = spr_str(str_list)
    if check_balance(u):
        return u + dfs(v)
    else:
        str_pls = '(' + dfs(v) + ')'
        u_pls = u[1:-1]
        u_refact = ''
        for i in u_pls:
            if i == '(':
                u_refact+=')'
            else:
                u_refact += '('
        return str_pls + u_refact
    
def solution(p):
    print(p)
    answer = ''
    return dfs(p)