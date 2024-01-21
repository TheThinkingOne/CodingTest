import sys
sys.stdin = open('input.txt','r')

N = int(input())  # 꽃의 개수

all_plus = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
March1st_to_Nov30th = 273

flowers = []  # 각 꽃의 정보를 저장할 리스트

def daySum(mon, day):
    if mon <= 2:
        return all_plus[mon + 10] + day
    else:
        return March1st_to_Nov30th + all_plus[mon - 1] + day


# 입력값을 받아서 리스트에 저장
for i in range(N):
    fullBloom = list(map(int, input().split()))
    bloomDate = daySum(fullBloom[0], fullBloom[1])  #fullBloom[0] = 월, fullBloom[1] = 일
    wiltDate = daySum(fullBloom[2], fullBloom[3])   # 꽃이 시들어가는 날짜를 숫자로 표현
    flowers.append((bloomDate, wiltDate))

# 꽃이 지는 날짜를 기준으로 정렬
flowers.sort(key=lambda x: (x[1], -x[0]))
print(flowers)

flowerCount = 0
current_flower = flowers[0]

for i in range(1, N):
    if flowers[i][0] > current_flower[1]:
        flowerCount += 1
        current_flower = flowers[i]

print(flowerCount)
