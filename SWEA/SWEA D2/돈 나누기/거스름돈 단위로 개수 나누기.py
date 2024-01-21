import sys
sys.stdin = open('input.txt', 'r')

change = [50000,10000,5000,1000,500,100,50,10]

T = int(input())
for i in range(T):
    Money = int(input())
    Data = []
    for j in range(len(change)):
        Data.append(Money//change[j])
        if Money // change[j] >= 1:
            Money -= (Money // change[j])*change[j]
    print(f"# {i+1}")
    for k in range(len(Data)):
        print(Data[k], end=' ')
    print()

    #     Data.append(Money % k)
    #     if (Money % k) >= 1:
    #         Money -= change[j]*(Money % change[j])
    # print(Data)


