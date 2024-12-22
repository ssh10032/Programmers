def solution(bridge_length, weight, truck_weights):
    c_num = 0
    c_weight = 0
    c_time = 0
    t_queue = []
    while True:
        if t_queue:
            if c_time==t_queue[0][1]+bridge_length:
                pass_truck = t_queue.pop(0)
                c_num-=1
                c_weight-=pass_truck[0]
        if truck_weights:
            if c_num+1<=bridge_length and c_weight+truck_weights[0]<=weight:
                truck_weight = truck_weights.pop(0)
                t_queue.append([truck_weight, c_time])
                
                c_num+=1
                c_weight+=truck_weight
        
        c_time+=1
        if not t_queue and not truck_weights:
            return c_time
    return c_time