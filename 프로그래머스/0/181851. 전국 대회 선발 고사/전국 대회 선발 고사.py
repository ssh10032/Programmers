def solution(rank, attendance):
    o_dict = dict(zip(rank, attendance))
    s_dict = sorted(o_dict.items())
    student_list = []
    for i, j in s_dict:
        if j:
            student_list.append(i)
        if len(student_list)==3:
            break
    return rank.index(student_list[0]) * 10000 + rank.index(student_list[1]) * 100 + rank.index(student_list[2])