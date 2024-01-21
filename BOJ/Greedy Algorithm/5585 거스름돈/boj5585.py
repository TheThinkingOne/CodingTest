import sys
sys.stdin = open('input.txt','r')

howMuch = int(input())
changelist = [500,100,50,10,5,1]

charge = 0
change = 1000 - howMuch

while change != 0:
    for i in range(len(changelist)):
        charge += change // changelist[i]
        change -= changelist[i] * (change // changelist[i])
        i += 1
    print(charge)
