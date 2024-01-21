def getSum(n):
    if n==1 : return 1

    else:
        return n + getSum(n-1)

print(getSum(6))