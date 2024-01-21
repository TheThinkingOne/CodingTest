import random
import time
def merge_sort(data):
    if len(data) <= 1: return data
    left = merge_sort(data[:len(data) // 2])
    right = merge_sort(data[len(data) // 2:])
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i];
            i += 1;
            k += 1
        else:
            data[k] = right[j];
            j += 1;
            k += 1

    if i == len(left):
        while j < len(right): data[k] = right[j]; j += 1;k += 1
    elif j == len(right):
        while i < len(left): data[k] = left[i]; i += 1;k += 1
    return data

data = [random.randint(1, 1000) for _ in range(100)]
# data = list(map(int, input().split()))

print(merge_sort(data)[:10])