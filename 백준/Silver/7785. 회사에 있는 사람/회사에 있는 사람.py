import sys

n = int(sys.stdin.readline())
employees = {}

for _ in range(n):
    name, status = map(str, sys.stdin.readline().rstrip().split())

    if status == "enter":
        employees[name] = 1
    else:
        del employees[name]
answer = list(employees.keys())
answer.sort(reverse=True)
print("\n".join(map(str, answer)))