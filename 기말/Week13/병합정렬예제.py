import sys
sys.stdin = open('input.txt', 'r')

def mergeSort(Data):
    if len(Data) <=1 : return Data
    left = mergeSort(Data[:len(Data)//2])
    right = mergeSort(Data[len(Data)//2:])

    #left index = i, right index = j, data index = k
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            Data[k] = left[i]
            i+= 1
            k+= 1
        else:
            Data[k] = right[j]
            j+=1
            k+=1

    return Data


Data = list(map(int, input().split()))

print(mergeSort(Data))




