import sys
sys.stdin = open('input2.txt', 'r')
#엑셀파일 참고

T = int(input())
for k in range(T):
    V, howmany, pos = map(int, input().split()) # V: 노드의 개수
    # 첫 케이스에서 L = 리프노드
    # 첫 케이스에서 v = 5, L = 3, where = 2
    Tree = [0 for _ in range(1001)]
    for i in range(howmany):
        where, what = map(int, input().split()) # where번 방에 what 이 들어있음
        Tree[where] = what

    # V - howmany 부터 시작!!
    for j in range(V - howmany, 0, -1):  # 2번방부터 시작
        Tree[j] = Tree[j * 2] + Tree[j * 2 + 1]
    # pos 위치에 있는 값과 그 자식들의 값의 합 출력
    print(f"#{k+1} {Tree[pos]}")


