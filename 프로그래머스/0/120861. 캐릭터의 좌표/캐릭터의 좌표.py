def solution(keyinput, board):
    # 초기 좌표 설정
    x, y = 0, 0
    
    # 맵의 최대 이동 가능 범위
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    # 방향키 입력에 따른 이동 처리
    for key in keyinput:
        if key == "up":
            y += 1
        elif key == "down":
            y -= 1
        elif key == "left":
            x -= 1
        elif key == "right":
            x += 1
        
        # 이동한 좌표가 맵의 경계를 벗어나지 않도록 조정
        if x > max_x:
            x = max_x
        elif x < -max_x:
            x = -max_x
        
        if y > max_y:
            y = max_y
        elif y < -max_y:
            y = -max_y
    
    # 최종 좌표 반환
    return [x, y]