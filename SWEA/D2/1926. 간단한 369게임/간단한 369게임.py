T = int(input())
for num in range(1, T + 1):
    str_num = str(num)
    clap_num = 0
    if '3' in str_num:
        clap_num+= str_num.count('3')
    if '6' in str_num:
        clap_num+= str_num.count('6')
    if '9' in str_num:
        clap_num+=  str_num.count('9')
    if clap_num==0:
        if num == T:
            print(str_num)
        else :
             print(str_num, end = ' ')
    else:
        if num == T:
            print('-' * clap_num)
        else:
            print('-' * clap_num, end = ' ')