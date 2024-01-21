def GetSome(n):
    if n == 0:
        return  # Base case
    print(n)
    GetSome(n - 1)
GetSome(5)
