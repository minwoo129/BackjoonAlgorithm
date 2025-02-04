import sys
import heapq

n = int(sys.stdin.readline())
heap = []
answers = []
for i in range(n):
    item = int(sys.stdin.readline())

    if item != 0:
        heapq.heappush(heap, item)
        continue

    if len(heap) == 0:
        answers.append(0)
        continue

    popItem = heapq.heappop(heap)
    answers.append(popItem)

for item in answers:
    print(item)

