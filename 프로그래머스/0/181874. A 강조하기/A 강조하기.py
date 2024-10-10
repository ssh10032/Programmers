def solution(myString):
    answer = []
    for i in myString:
        if i == "a":
            answer.append("A")
        elif i!= "A" and i.isupper()==True:
            answer.append(i.lower())
        else:
            answer.append(i)
    return ''.join(answer)