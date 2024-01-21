Data = [2, 4, 7, 9, 11, 19, 23]

def LookforKey(key):
    start = 0
    end = len(Data) - 1
    while start <= end:
        mid = (start + end) // 2
        if Data[mid] == key:
            return mid  # 값을 찾으면 인덱스를 반환
        elif Data[mid] < key:
            start = mid + 1
        else:  # Data[mid] > key 일 경우
            end = mid - 1
    return -1  # 값을 찾지 못한 경우 -1을 반환

key = 23
result = LookforKey(key)
if result != -1:
    print("찾음")
    print("인덱스:", result)  # 찾은 값의 인덱스 출력
else:
    print("찾지 못함")
