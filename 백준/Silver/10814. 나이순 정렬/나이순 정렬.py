import sys

n = int(sys.stdin.readline())
inputArr = []

for _ in range(n):
    age, name = map(str, sys.stdin.readline().rstrip().split())
    inputArr.append({ 'age': int(age), 'name': name })

inputArr = sorted(inputArr, key = lambda x: x['age'])

for item in inputArr:
    print(str(item['age']) + " " + item['name'])