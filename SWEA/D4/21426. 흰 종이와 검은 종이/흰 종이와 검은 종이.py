def cal_intersection(white, black):
    x_left = max(white[0], black[0])
    y_bottom = max(white[1], black[1])
    x_right = min(white[2], black[2])
    y_top = min(white[3], black[3])
    if x_left < x_right and y_bottom < y_top:
        return [x_left, y_bottom, x_right, y_top]
    else:
        return None
def cal_area(rect):
    return (rect[2]-rect[0]) * (rect[3]-rect[1])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    w_paper = list(map(int, input().split()))
    b_paper1 = list(map(int, input().split()))
    b_paper2 = list(map(int, input().split()))

    intersection1 = cal_intersection(w_paper, b_paper1)
    if intersection1:
        white_area = cal_area(w_paper)-cal_area(intersection1)
    else:
        white_area = cal_area(w_paper)

    intersection2 = cal_intersection(w_paper, b_paper2)
    if intersection2:
        white_area = white_area-cal_area(intersection2)

    intersect_both = cal_intersection(intersection1, b_paper2) if intersection1 else None
    if intersect_both:
        white_area += cal_area(intersect_both)

    if white_area!=0:
        print("YES")
    else:
        print("NO")