def solution(nums):
    total_num = len(nums)
    # if set(nums)>=len(nums)
    num_dict = {}
    for i in nums:
        if i in num_dict.keys():
            num_dict[i]+=1
        else:
            num_dict[i]=1
    print(num_dict)
    # return 0
    return min(len(set(nums)),len(nums)/2)