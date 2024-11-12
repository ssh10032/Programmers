T = int(input())
for test_case in range(1, T + 1):
    cup_list, sound_num = map(str, input().split())
    sound_num = int(sound_num)
    if sound_num==0:
        print('#{} {}'.format(test_case, cup_list.index('o')))
    elif sound_num % 2 == 0:
        if cup_list.index('o')==1:
            print('#{} 1'.format(test_case))
        else:
             print('#{} 0'.format(test_case))
    else :
        if cup_list.index('o')==1:
            print('#{} 0'.format(test_case))
        else:
             print('#{} 1'.format(test_case))
    

