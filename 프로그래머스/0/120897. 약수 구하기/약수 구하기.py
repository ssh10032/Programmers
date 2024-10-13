def solution(n):
    answer = [1, n]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if n==i**2:
                answer.append(i)
            else:
                answer.append(i)
                answer.append(n//i)
    answer.sort()
    return answer if n!=1 else [1]