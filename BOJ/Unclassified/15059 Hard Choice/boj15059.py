import sys
sys.stdin = open('input.txt', 'r')

foods = list(map(int,input().split()))
order = list(map(int,input().split()))
insufficient = 0

for i in range(len(foods)):
    for j in range(len(foods)):
        if i == j:
            if foods[i] < order[j]:
                insufficient += order[j] - foods[i]

print(insufficient)