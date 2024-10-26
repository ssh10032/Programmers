def solution(n):
    move_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_idx = 0
    answer = [[0] * n for _ in range(n)]
    
    x, y = 0, 0
    num = 1
    
    while num <= n*n:
        answer[x][y] = num
        num += 1
        
        dx, dy = move_direction[direction_idx][0], move_direction[direction_idx][1]
        nx, ny = x + dx, y + dy
        
        if not (0<=nx<n and 0<=ny<n and answer[nx][ny]==0):
            direction_idx = (direction_idx+1)%4
            dx, dy = move_direction[direction_idx][0], move_direction[direction_idx][1]
            nx, ny = x + dx, y + dy
            
        x, y = nx, ny
    return answer