import sys
sys.stdin = open('input.txt', 'r')

Card = int(sys.stdin.readline())
Deck = []

for _ in range(1,Card+1):
    Deck.append(_)

while len(Deck) > 1:
    Deck.pop(0)
    Deck.append(Deck.pop(0))
    # Deck[0], Deck[-1] = Deck[-1], Deck[0]

print(Deck[0])