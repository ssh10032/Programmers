import math

def solution(progresses, speeds):
    complete_times = []
    complete_counts = []
    for progress, speed in zip(progresses, speeds):
        complete_time = math.ceil((100 - progress) / speed)
        complete_times.append(complete_time)
    max_time = complete_times[0]
    complete_count = 0
    for i in complete_times:
        if max_time>=i:
            complete_count+=1
        else:
            max_time = i
            complete_counts.append(complete_count)
            complete_count = 1
    complete_counts.append(complete_count)
    return complete_counts