import heapq

def find_min_repair_time(way_matrix):
    n = len(way_matrix)
    min_time = [[float('inf')] * n for _ in range(n)]
    min_time[0][0] = way_matrix[0][0]

    heap = [(way_matrix[0][0], 0, 0)]

    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    while heap:
        current_time, x, y = heapq.heappop(heap)

        if x == n - 1 and y == n - 1:
            return current_time

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_time = current_time + way_matrix[nx][ny]

                if new_time < min_time[nx][ny]:
                    min_time[nx][ny] = new_time
                    heapq.heappush(heap, (new_time, nx, ny))

T = int(input())

for test_case in range(1, T + 1):
    matrix_len = int(input())
    way_point = [list(map(int, input().strip())) for _ in range(matrix_len)]
    min_cost = find_min_repair_time(way_point)
    print('#{} {}'.format(test_case, min_cost))