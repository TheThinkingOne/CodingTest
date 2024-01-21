import sys

li = [[1, 5, 3], [2, 5, 7], [5, 3, 5]]
chk = [False] * 3
m = sys.maxsize

def backtracking(row, score):
    global m

    if row == 3:  # 재귀함수를 마치는 조건
        if score < m:
            m = score
        return

    for i in range(3):
        if not chk[i]:  # 백트래킹에서의 한정조건
            chk[i] = True
            backtracking(row + 1, score + li[row][i])
            chk[i] = False

backtracking(0, 0)
print(m)
