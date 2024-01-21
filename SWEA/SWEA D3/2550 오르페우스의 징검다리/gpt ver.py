import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def move_along(leg, change, life):
    n = len(leg)
    played = 0
    current_point = 0

    while current_point < n:
        next_point = min(current_point + change, n)
        found = False

        for i in range(next_point - 1, current_point - 1, -1):
            if leg[i] == 0:
                leg[i] = 1
                played += 1
                found = True
                current_point = i
                break

        if not found:
            return -1

        life -= 1

        if life <= 0:
            return -1

    return played


for i in range(T):
    leg = list(map(int, input().strip()))
    change, life = map(int, input().split())
    result = move_along(leg, change, life)
    print(f"{i + 1} {result}")





