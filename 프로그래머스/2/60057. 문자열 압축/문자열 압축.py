def solution(s):
    answer = 0
    str_len = len(s)
    chk_len = str_len // 2

    results = []
    results.append(len(s))
    for i in range(1, chk_len + 1):
        count = 1
        result = 0
        for j in range(0, str_len - i, i):
            if s[j:j + i] == s[j + i:j + 2 * i]:
                count += 1
                if j + i >= str_len - i:
                    result += i+len(str(count))
            else:
                if count > 1:
                    if j + i >= str_len - i:
                        result += (i + len(str(count))) + len(s[j+i:])
                    else:
                        result += (i + len(str(count)))
                else:
                    if j + i >= str_len - i:
                        result += i + len(s[j+i:])
                    else:
                        result += i
                count = 1
        results.append(result)
    return min(results)