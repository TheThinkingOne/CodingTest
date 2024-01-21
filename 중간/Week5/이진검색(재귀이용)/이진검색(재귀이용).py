import sys
sys.stdin = open('input.txt', 'r') #파일에서 읽을 때

def binarySearchR(start,end,key):
    if start > end : return False
    middle = (start+end)//2 #(start+end)>>1
    if key == Data[middle]: #찾았다!
        return True
    elif key < Data[middle]:
        return binarySearchR(start, middle-1, key)
    elif key > Data[middle]:
        return binarySearchR(middle+1,end,key)

Data = list(map(int, input().split()))
Data.sort()

key=55 #55찾기
print(binarySearchR(0,6,key))