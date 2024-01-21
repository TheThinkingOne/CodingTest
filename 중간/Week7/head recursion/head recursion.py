def GetSome(n):
    if n == 0:
        return  # Base case
    GetSome(n - 1)  # head Recursive Call
    print(n)

GetSome(5)
