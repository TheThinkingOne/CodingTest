import sys
sys.stdin = open('input.txt', 'r')

L = int(input())
Start = 0
count = 0
findingWay = [1, 2, 3, 4, 5]

def chaser(Start):
    global count
    while Start < L:
        max_step = 0
        for i in findingWay:
            if Start + i <= L:
                max_step = max(max_step, i)
        Start += max_step
        count += 1
    print(count)

chaser(Start)



# for i in findingWay:
#     while newPoint == L:
#         newPoint = Start + i
#         count += 1
#     print(count)







