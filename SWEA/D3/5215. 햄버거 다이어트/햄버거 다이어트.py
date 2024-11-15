def max_hamburger_score(gd_list, cal_limit):
    dp = [0] * (cal_limit + 1)

    for score, cal in gd_list:
        for j in range(cal_limit, cal - 1, -1):
            dp[j] = max(dp[j], dp[j - cal] + score)

    return dp[cal_limit]


T = int(input())

for test_case in range(1, T + 1):
    gd_num, cal_limit = map(int, input().split())
    gd_list = []
    for _ in range(gd_num):
        gd_score, gd_cal = map(int, input().split())
        gd_list.append((gd_score, gd_cal))

    result = max_hamburger_score(gd_list, cal_limit)
    print(f'#{test_case} {result}')