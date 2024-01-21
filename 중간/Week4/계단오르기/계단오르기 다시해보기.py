ans = 0

def 계단오르기(here):
    global ans
    if here > howmany : return
    if here == howmany:
        ans+=1 #계단 다 오르면 기록
        return
    계단오르기(here+1)
    계단오르기(here+2)



howmany = 5
계단오르기(0)
print(ans)