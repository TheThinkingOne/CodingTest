Queue = []

for soldiers in range(1,42):
    Queue.append(soldiers)
print(Queue)

while len(Queue)!=2: #큐의 길이가 2가 아닐때까지 반복
    alive1 = Queue.pop(0)
    alive2 = Queue.pop(0)
    dead = Queue.pop(0)
    Queue.append(alive1)
    Queue.append(alive2)

print(Queue)




