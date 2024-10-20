def solution(polynomial):
    terms = polynomial.split(' + ')
    
    coefficients = {'x': 0, '': 0}  # 'x'에 대한 계수, 상수항에 대한 계수
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                coefficients['x'] += 1
            else:
                coefficients['x'] += int(term[:-1]) 
        else:
            coefficients[''] += int(term)
    
    result = []
    if coefficients['x'] != 0:
        if coefficients['x'] == 1:
            result.append('x')
        else:
            result.append(f"{coefficients['x']}x")
    
    if coefficients[''] != 0:
        result.append(str(coefficients['']))

    return ' + '.join(result) if result else '0'