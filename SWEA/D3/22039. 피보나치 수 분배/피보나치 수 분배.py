T = int(input())
for test_case in range(1, T + 1):
    fibo_len = int(input())
    if (fibo_len+1)%3==0:
        iter_num = (fibo_len-2)//3
        print('AB'+'AAB'*iter_num)
    elif fibo_len%3==0:
        iter_num = fibo_len//3
        print('AAB'*iter_num)
    else:
        print('impossible')