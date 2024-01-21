import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    P, Q, R, S, W = map(int,input().split())
    pay = 0
    if P*W <= Q:
        pay = P*W
    elif P*W >= Q:
        pay = Q
    if W >= R:
        if P*W >= Q+(W-R)*S:
            pay = Q+(W-R)*S
        elif P*W <= Q+(W-R)*S:
            pay = P*W
    print(f"#{i+1} {pay}")


