import sys
sys.stdin = open('input.txt','r')

N, M = map(int,input().split())
cards = list(map(int,input().split()))
cards.sort()
cardSum = 0
#print(cards)

while M != 0:
    cardSum = cards[0] + cards[1]
    cards[0], cards[1] = cardSum, cardSum
    cards.sort()
    M -= 1

print(sum(cards))

