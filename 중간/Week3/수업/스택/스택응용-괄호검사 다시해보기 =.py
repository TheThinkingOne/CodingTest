import sys
sys.stdin = open('input.txt', 'r')

Warehouse = []
things = input()
ans = 0

for i in range(len(things)):
    if things[i] == '(':
        Warehouse.append(things[i])
    elif Warehouse and (things[i]==')' and things[-1]==')'):
        Warehouse.pop()
    else: break

if not Warehouse:
    ans = 1
    print(ans)


