def solution(participant, completion):
    # 참가자 딕셔너리 생성
    p_dict = {}
    for i in participant:
        if i in p_dict:
            p_dict[i] += 1
        else:
            p_dict[i] = 1
    
    # 완주자 처리
    for j in completion:
        if j in p_dict:
            p_dict[j] -= 1
            if p_dict[j] == 0:
                del p_dict[j]
    
    # 남아 있는 이름 반환
    for key in p_dict:
        return key
