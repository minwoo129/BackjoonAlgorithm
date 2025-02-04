def check(number):
    length = len(number)
    
    if length == 1 or '1' not in number or '0' not in number:
        return True
    
    mid = length // 2
    
    if number[mid] == '0':
        return False
    
    return check(number[:mid]) and check(number[mid+1:])

def solution(numbers):
    answer = []
    bin_numbers = [ bin(x)[2:] for x in numbers ]
    bin_list = [ 2**x - 1 for x in range(50) ]
    
    for number in bin_numbers:
        length = len(number)
        for num in bin_list:
            if num >= length:
                number = '0'*(num-length)+number
                break
        answer.append(1 if check(number) else 0)
        
    return answer