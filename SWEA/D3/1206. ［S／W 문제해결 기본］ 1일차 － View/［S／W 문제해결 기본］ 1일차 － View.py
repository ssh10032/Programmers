for test_case in range(1, 11):
    good_apt_num = 0
    apt_num = int(input())
    apt_list = list(map(int, input().split()))
    for apt_idx in range(2, apt_num-2):
        max_apt = max(apt_list[apt_idx-2], apt_list[apt_idx-1], apt_list[apt_idx+1], apt_list[apt_idx+2])
        if max_apt > apt_list[apt_idx]:
            pass
        else:
            good_apt_num += apt_list[apt_idx] - max_apt
    print('#{} {}'.format(test_case, good_apt_num))