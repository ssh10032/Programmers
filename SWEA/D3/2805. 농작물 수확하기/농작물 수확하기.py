T = int(input())

for test_case in range(1, T+1):
    farm_len = int(input())
    mid_idx = (farm_len-1)//2
    cultivate_value = 0
    # print('mid idx is {}'.format(mid_idx))
    for row in range(farm_len):
        row_dist = abs(row - mid_idx)
        # print('row {} row_dist is {}'.format(row, row_dist))
        row_list = str(input().strip())
        # print('row_list is {}'.format(row_list))
        for col in range(farm_len):
            if row_dist <= col < farm_len-row_dist:
                cultivate_value += int(row_list[col])
    print('#{} {}'.format(test_case, cultivate_value))