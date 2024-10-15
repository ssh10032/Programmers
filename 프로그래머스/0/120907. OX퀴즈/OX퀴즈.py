def solution(quiz):
    ox_list = []
    for i in quiz:
        eq_list = i.split()
        operator = eq_list[1]
        if operator == '+':
            if int(eq_list[0])+int(eq_list[2])==int(eq_list[4]):
                ox_list.append("O")
            else:
                ox_list.append("X")
        else:
            if int(eq_list[0])-int(eq_list[2])==int(eq_list[4]):
                ox_list.append("O")
            else:
                ox_list.append("X")
                
    return ox_list