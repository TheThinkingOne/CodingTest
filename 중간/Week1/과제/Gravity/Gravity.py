import sys
sys.stdin = open('input.txt', 'r')

howmany = int(input())

for tc in range(howmany):
    blocks = int(input())
    block_lens = list(map(int, input().split()))

    maxVal = block_lens[0]
    count = 0

    for i in block_lens:
        if i >= maxVal:
            maxVal = i
        else:
            count += 1
    print(f"#{tc+1} {count}")

    # for where in range(blocks):
    #     if(block_lens[where] < block_lens[min]):
    #         min = where
    #     block_lens[blocks], block_lens[min] = block_lens[min], block_lens[blocks]
    # print(block_lens)

# import sys
# sys.stdin = open('input.txt', 'r')
#
# repeat = int(input())
#
# for i in range(repeat):
#     Box = int(input())
#     nlist = list(map(int, input().split()))
#
#     maxN = nlist[0]
#     count = 0
#
#     for j in nlist:
#         if j >= maxN:
#             maxN = j
#         else:
#             count += 1
#
#     print("#%d %d" % (i + 1, count))




