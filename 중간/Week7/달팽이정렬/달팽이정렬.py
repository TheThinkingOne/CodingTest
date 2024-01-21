import random
import time

N = 5

def ptf(a):
    for row in a:
        for elem in row:
            print(f"{elem:2}" if elem != 0 else "  ", end="|")
        print()
    print("-"*(N*3-1))

def snail_sort(a):
    arr2 = [row[:] for row in a]
    flat_list = [a for sublist in a for a in sublist]
    flat_list.sort()

    revol = N
    num = 0
    n1 = 0
    n2 = -1
    A = 1

    for i in range(N * N):
        index = i
        for j in range(i + 1, N * N):
            if flat_list[index] > flat_list[j]:
                index = j
        flat_list[i], flat_list[index] = flat_list[index], flat_list[i]

    while True:
        for i in range(revol):
            n2 += A
            a[n1][n2] = flat_list[num]
            num += 1

        revol -= 1

        if revol == 0:
            break

        for i in range(revol):
            n1 += A
            a[n1][n2] = flat_list[num]
            num += 1

        A = -A

if __name__ == "__main__":
    arr = [[0 for _ in range(N)] for _ in range(N)]
    p1 = arr

    random.seed(time.time())

    for i in range(N * N):
        p1[i // N][i % N] = random.randint(1, N * N)

        for j in range(i):
            if p1[i // N][i % N] == p1[j // N][j % N]:
                i -= 1
                break

    print("\n  정렬 전")
    ptf(arr)
    snail_sort(arr)
    print("\n  정렬 후")
    ptf(arr)
