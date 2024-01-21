#p.31 참고
#이진검색은 자료가 정렬되어 있는 상태여야 한다.
Data = [2,4,7,9,11,19,23]

def FindThis(key):
    start = 0
    end = len(Data)-1
    while start<=end:
        mid = (start + end)>>1 # 또는 (start+end)//2, mid=3
        if Data[mid] == key: #mid=3 일때의 값이 key값이면
            return True
        elif Data[mid] < key: # 키값이 데이터의 3번째보다 크면
            start = mid+1 #탐색범위 재지정, mid=4로 시작
        else:
            end = mid-1 #아니면 mid값을 2로 시작(탐색범위 축소)
    return False


key = 11
if FindThis(key):
    print("Gotcha!")
else:
    print("어디갔지?")