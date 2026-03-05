import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    
    a = a % 10
    
    if a == 0:
        print(10)
        continue
    if a == 1 or a == 5 or a == 6:
        print(a)
        continue
    
    if a == 4 or a == 6:
        b = b % 2
        
        if b == 1:
            print(a)
        else:
            print((a*a)%10)
        continue
    
    
    b = b % 4
    
    if b == 0:
        print((a**4)%10%10%10)
    else:
        print((a**b)%10%10%10)
        
    
    