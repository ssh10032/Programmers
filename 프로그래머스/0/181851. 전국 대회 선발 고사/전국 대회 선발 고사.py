def solution(rank, attendance):
    s_list = sorted([(v, i) for i, v in enumerate(rank) if attendance[i]])
    return s_list[0][1] * 10000 + s_list[1][1] * 100 + s_list[2][1]