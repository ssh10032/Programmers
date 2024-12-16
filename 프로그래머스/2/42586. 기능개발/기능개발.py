import math

def solution(progresses, speeds):
    complete_times = []
    complete_counts = []
    for progress, speed in zip(progresses, speeds):
        complete_time = math.ceil((100 - progress) / speed)
        complete_times.append(complete_time)
    max_time = 0
    complete_count = 0
    for i in range(len(complete_times)):
        if i == 0:
            max_time = complete_times[i]
            complete_count=1
        else:
            if max_time>=complete_times[i]:
                complete_count+=1
                if i == len(complete_times)-1:
                    complete_counts.append(complete_count)
            else:
                max_time = complete_times[i]
                complete_counts.append(complete_count)
                complete_count = 1
                if i == len(complete_times)-1:
                    complete_counts.append(complete_count)
    return complete_counts