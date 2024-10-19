def solution(array):
    c_seven = 0
    for i in array:
        c_seven += str(i).count("7")
    return c_seven