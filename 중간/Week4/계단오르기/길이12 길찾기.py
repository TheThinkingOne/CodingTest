ans = 0


def findWay(here):
    global ans
    if here > howmany: return
    if here == howmany:
        ans += 1
        return
    findWay(here + 1)
    findWay(here + 2)
    findWay(here + 3)
    findWay(here + 4)
    findWay(here + 5)

howmany = 12
findWay(0)
print(ans)