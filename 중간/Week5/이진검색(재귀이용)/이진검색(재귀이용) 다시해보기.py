import sys
sys.stdin = open('input.txt', 'r') #파일에서 읽을 때

#이진검색은 이미 자료가 정렬되어 있을때만 사용가능
def SearchKey(start, end, key):
    if start > end : return False
    middle = (start+end)//2
    if key == Sinners[middle]:
        return True
    elif key < Sinners[middle]:
        #키값이 중간값보다 작으므로 범위를 좁힘
        return SearchKey(start, middle-1, key)
    elif key > Sinners[middle]:
        #키값이 중간값보다 크므로 범위를 좁힘
        return SearchKey(middle+1, end, key)


Sinners = list(map(int,input().split()))
Sinners.sort()

key=55
print(SearchKey(0,6,key))
