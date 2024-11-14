def count_score(score_list):
    possible_scores = {0}
    for score in score_list:
        new_scores = set()
        for current_score in possible_scores:
            new_scores.add(current_score + score)
        possible_scores.update(new_scores)
    return len(possible_scores)

T = int(input())
for test_case in range(1, T + 1):
    total_q = int(input())
    score_list = list(map(int, input().split()))
    print('#{} {}'.format(test_case, count_score(score_list)))