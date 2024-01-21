def Fibonachi(n):
    if n == 0 or n == 1: return 1

    else:
        return Fibonachi(n-1) + Fibonachi(n-2)

print(Fibonachi(5))

## 0 1 1 2 3 5 8 13 21 34 ....