def solution(board, k):
    rows = [i for i in range(0,len(board))]
    cols = [i for i in range(0,len(board[0]))]
    answer = []
    for i in rows:
        for j in cols:
            if i+j<=k:
                answer.append(board[i][j])
    return sum(answer)