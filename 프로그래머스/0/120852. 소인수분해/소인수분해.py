def solution(n):
    answer = []
    def is_prime(x):
        if x < 2:
            return False
        else:
            for i in range(2, int(x**0.5)+1):
                if x%i==0:
                    return False
        return True
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            if is_prime(i):
                answer.append(i)
            if i != n // i and is_prime(n // i):
                answer.append(n // i)
    print(answer)
    return sorted(answer)