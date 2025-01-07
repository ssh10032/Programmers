def solution(sizes):
    
    rotated_size = [[max(size), min(size)] for size in sizes]
    max_x = max(size[0] for size in rotated_size)
    max_y = max(size[1] for size in rotated_size)
        
    return max_x * max_y