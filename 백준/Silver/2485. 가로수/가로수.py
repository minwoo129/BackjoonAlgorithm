import sys

n = int(sys.stdin.readline())
pos = []
sub = []
answer = 0

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(n):
    pos.append(int(sys.stdin.readline()))

for i in range(1, n):
    sub.append(pos[i] - pos[i - 1])

gcdVal = sub[0]
for i in range(1, len(sub)):
    gcdVal = gcd(gcdVal, sub[i])

for s in sub:
    answer += s // gcdVal - 1
print(answer)

