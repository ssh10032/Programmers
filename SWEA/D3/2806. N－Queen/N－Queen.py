def is_safe(row, col, queens):
    for r, c in enumerate(queens):
        if c == col or abs(row-r) == abs(col-c):
            return False
    return True

def solve_n_queens(n, row, queens):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if is_safe(row, col, queens):
            queens.append(col)
            count += solve_n_queens(n, row + 1, queens)
            queens.pop()
    return count

def count_n_queen_solutions(n):
    return solve_n_queens(n, 0, [])

T = int(input())

for test_case in range(1, T + 1):
    matrix_len = int(input())
    print('#{} {}'.format(test_case, count_n_queen_solutions(matrix_len)))