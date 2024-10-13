def solution(numbers):
    numb_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    num_str = ''
    num_int = ''
    for char in numbers:
        num_str+=char
        if num_str in numb_dict:
            num_int+=numb_dict[num_str]
            num_str=''
    print(num_int)
    return int(num_int)