def f(n, k):
    if n == 1:
        return k if k <= 2 else k-1
    div = 5 ** (n-1)
    cnt1 = 4 ** (n-1)
    loc = k // div
    
    if k % div == 0:
        loc -= 1
    
    if loc < 2:
        return cnt1*loc + f(n-1, k-(loc*div))
    elif loc == 2:
        return cnt1*loc
    else:
        return cnt1*(loc-1) + f(n-1, k-(loc*div))
        

def solution(n, l, r):
    answer = 0
    
    answer = f(n, r) - f(n, l-1)
    return answer