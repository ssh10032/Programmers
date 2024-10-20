def solution(dots):
    x_list = []
    y_list = []
    for x, y in dots:
        x_list.append(x)
        y_list.append(y)
    return (max(x_list)-min(x_list)) * (max(y_list)-min(y_list))