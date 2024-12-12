def solution(participant, completion):
    # 참가자 딕셔너리 생성
    p_dict = {}
    for i in participant:
        if i in p_dict:
            p_dict[i] += 1
        else:
            p_dict[i] = 1
    
    for j in completion:
        if j in p_dict.keys():
            p_dict[j]-=1
            if p_dict[j]==0:
                del p_dict[j]
    # print(p_dict)
    for key, value in p_dict.items():
        print(key)
        return key
