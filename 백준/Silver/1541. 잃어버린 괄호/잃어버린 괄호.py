import sys

exp = sys.stdin.readline().rstrip().split("-")
nums = []

for s in exp:
    sArr = s.split("+")
    num = 0
    for s1 in sArr:
        num += int(s1)
    nums.append(num)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]
print(result)
