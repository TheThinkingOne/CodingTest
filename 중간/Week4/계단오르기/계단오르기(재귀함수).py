#계단을 한칸 혹은 두칸 오르기
#목표 계단층수에 갈 수 있는 경우의 수 구하는 프로그램
ans=0
def meaninglessName(here):
    global ans #ans를 전역변수로 선언(파이썬에선 글로벌)
    if here > howmany: return
    if here == howmany:
        ans+=1
        return
    meaninglessName(here+1)
    meaninglessName(here+2)

howmany = 5 #계단은 총 howmany칸
meaninglessName(0)
print(ans)