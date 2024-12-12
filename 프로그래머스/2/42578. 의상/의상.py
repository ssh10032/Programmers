def solution(clothes):
    answer=1
    cloth_dict = {}
    for name, cat in clothes:
        if cat in cloth_dict:
            cloth_dict[cat].append(name)
        else:
            cloth_dict[cat] = [name]
    for key in cloth_dict:
        # print(cloth_dict[key])
        # print(len(cloth_dict[key]))
        answer = answer * (len(cloth_dict[key])+1)
    return answer-1