T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(1, N+1)]
    max = 0
    i, j = 0, 0
    iter_num = (N-M+1)**2
    for _ in range(0, iter_num):
        if i+M > N or j+M >N:
            pass
        sum = 0
        for x in range(0,M):
            for y in range(0, M):
                sum += num_list[i+x][j+y]
        if max < sum:
            max = sum
        if i+M == N:
            i=0
            j+=1
        else:
            i+=1
    print('#{} {}'.format(test_case, max))