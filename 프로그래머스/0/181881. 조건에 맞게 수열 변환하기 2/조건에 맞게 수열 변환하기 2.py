def solution(arr):
    def transform(arr):
        return [
            num // 2 if num >= 50 and num % 2 == 0 else num * 2 + 1 if num < 50 and num % 2 == 1 else num
            for num in arr
        ]

    x = 0
    while True:
        new_arr = transform(arr)
        if new_arr == arr:
            return x
        arr = new_arr
        x += 1