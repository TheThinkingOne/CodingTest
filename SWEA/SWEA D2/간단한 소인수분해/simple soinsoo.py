import sys
sys.stdin = open('input.txt','r')

Primefactors = [2,3,5,7,11]

T = int(input())
for i in range(T):
    Number = int(input())
    count = [0]*5
    for j in range(len(Primefactors)):
        while Number % Primefactors[j] == 0:
            Number = Number // Primefactors[j]
            count[j] += 1
    print(f"#{i+1} {' '.join(map(str, count))}")

# def soinsoo(num):
#     if Number / Primefactors[j] == 0:
#         soinsoo(Number / Primefactors[j])









