# def SolveTowers(n, Start, to, spare): #p.84~
#     if n==1:
#         print(Start + " 에서 " + to + " 로 이동")
#         return
#     SolveTowers(n-1, Start, spare, to)
#     SolveTowers(1,Start, to, spare)
#     SolveTowers(n-1,Start, to, spare)
#
# SolveTowers(3, 'from','to','spare')

def SolveTowers(n, Start, to, spare):
    if n == 1:
        print(Start + " 에서 " + to + " 로 블록 이동")
        return
    SolveTowers(n - 1, Start, spare, to)
    print(Start + " 에서 " + to + " 로 블록 이동")  # 이동 메시지 출력
    SolveTowers(n - 1, spare, to, Start)

SolveTowers(3, 'A', 'C', 'B')
