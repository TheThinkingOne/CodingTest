Queue = []

# Queue.append(1)
# Queue.append(2)
# Queue.append(3)
# Queue.append(4)

for now in range(1,5):
    Queue.append(now)
print(Queue)

# print(Queue.pop(0))
# print(Queue.pop(0))
# print(Queue.pop(0))
# print(Queue.pop(0))

while Queue:
    print(Queue.pop(0))
