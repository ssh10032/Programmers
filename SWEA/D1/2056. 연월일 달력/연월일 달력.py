T = int(input())
days = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31, 2:28, 4:30, 6:30, 9:30,11:30}
for test_case in range(1, T + 1):
    a = str(input())  
    year = a[0:4]
    month = a[4:6]
    day = a[6:]
    if 0<int(month)<13 and 0<int(day)<=days[int(month)]:
        print("#{} {}/{}/{}".format(test_case, year, month, day))
    else:
        print("#{} -1".format(test_case))