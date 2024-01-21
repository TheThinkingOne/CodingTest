import sys
sys.stdin = open('input.txt', 'r')

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count_arr = [0] * (max_val - min_val + 1)
    result = [0] * len(arr)

    for num in arr:
        count_arr[num - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for num in reversed(arr):
        result[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    return result

# 예시
arr = [2, 4, 1, 0, 3, 2, 1, 0, 3, 4]
sorted_arr = counting_sort(arr)
print(sorted_arr)
