import sys
import heapq

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

while heap:
    print(heapq.heappop(heap))
