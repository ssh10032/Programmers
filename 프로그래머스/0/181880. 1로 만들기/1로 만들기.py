def solution(num_list):
    n=0
    for i in range(len(num_list)):
        while(num_list[i]!=1):
            if num_list[i]%2==0:
                num_list[i]=num_list[i]/2
                n+=1
            elif num_list[i]%2!=0:
                num_list[i] = (num_list[i]-1)/2
                n+=1
    return n