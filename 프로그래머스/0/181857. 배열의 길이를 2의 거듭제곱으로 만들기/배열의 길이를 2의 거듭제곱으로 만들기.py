def solution(arr):
    length = len(arr)
    i=0
    while(True):
        if length==2**i:
            return arr
        elif length>2**i and length<2**(i+1):
            arr+=[0]*(2**(i+1)-length)
            return arr
        i+=1
    return arr