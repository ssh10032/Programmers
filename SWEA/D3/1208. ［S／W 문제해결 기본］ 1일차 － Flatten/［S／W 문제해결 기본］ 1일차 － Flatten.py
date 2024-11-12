for test_case in range(1, 11):
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    box_list = list(map(int, input().split()))
    box_list.sort()
    for _ in range(1, T+1):
        min_box = min(box_list)
        min_idx = box_list.index(min_box)
        box_list[min_idx]+=1
        max_box = max(box_list)
        max_idx = box_list.index(max_box)
        box_list[max_idx]-=1
    dist = max(box_list)-min(box_list)
    print('#{} {}'.format(test_case, dist))