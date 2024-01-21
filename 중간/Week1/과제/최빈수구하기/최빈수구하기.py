import sys

sys.stdin = open('input.txt', 'r')

# 각 그룹에서 최빈값을 찾는 함수
def find_mode(grades):
    freq = [0] * 101
    mode = 0  # 최빈값
    for grade in grades:
        freq[grade] += 1
        if freq[grade] >= freq[mode]:
            mode = grade
    return mode

# 그룹 개수를 읽음
num_groups = int(input()) #첫번째 줄의 10이라는 숫자를 불러옴

#for문을 통해 차례로 한문장씩 번갈아가며 읽어옴
for tc in range(1, num_groups + 1):
    num_grades = int(input())  # 그룹 내 숫자의 개수
    grades = list(map(int, input().split()))  # 그룹 내 숫자들을 리스트로 읽음
    mode = find_mode(grades)  # 최빈값을 찾음
    print(f"#{tc} {mode}")




# def counting_sort(arr):
#     # 입력 배열에서 최댓값과 최솟값을 찾아서 범위를 결정합니다.
#     max_val = max(arr)
#     min_val = min(arr)
#
#     # 카운팅 배열을 초기화합니다.
#     count_array = [0] * (max_val - min_val + 1)
#
#     # 입력 배열을 순회하며 각 요소의 빈도를 세어 카운팅 배열에 저장합니다.
#     for num in arr:
#         count_array[num - min_val] += 1
#
#     # 정렬된 결과를 저장할 배열을 초기화합니다.
#     sorted_array = []
#
#     # 카운팅 배열을 순회하며 정렬된 결과를 만듭니다.
#     for i, count in enumerate(count_array):
#         sorted_array.extend([i + min_val] * count)
#
#     return sorted_array
#
#
# # 테스트를 위한 입력 배열
# arr = [4, 2, 2, 8, 3, 3, 1]
# sorted_arr = counting_sort(arr)
# print(sorted_arr)


