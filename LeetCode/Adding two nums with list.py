l1 = [2,4,3]
l2 = [5,6,4]
l3 = []

if len(l1) > len(l2):
    for i in range(-1, -len(l1) -1, -1):
        for j in range(-1, -len(l2) -1, -1):
            for k in range(-1, -len(l1) -1, -1):
                if i == j:
                    if l1[i]+l2[j]>=10:
                        l3[k] = l1[i]+l2[j]-10
                        l3[k-1] += 1
                else:
                    l3[k] = l1[i]


elif len(l2) > len(l1):
    for i in range(-1, -len(l1) -1, -1):
        for j in range(-1, -len(l2) -1, -1):
            for k in range(-1, -len(l2) - 1, -1):
                if i == j:
                    if l1[i] + l2[j] >= 10:
                        l3[k] = l1[i]+l2[j]-10
                        l3[k - 1] += 1
                else:
                    l3[k] = l2[j]



# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# l3 = []
#
# # 리스트의 길이가 더 큰 리스트를 선택합니다.
# longer_list = l1 if len(l1) > len(l2) else l2
#
# # 리스트의 길이가 더 큰 리스트의 길이만큼 l3 리스트를 초기화합니다.
# for i in range(len(longer_list)):
#     l3.append(0)
#
# # 두 리스트의 합을 계산합니다.
# for i in range(-1, -len(longer_list) - 1, -1):
#     for j in range(-1, -len(longer_list) - 1, -1):
#         for k in range(-1, -len(longer_list) - 1, -1):
#             if i == j:
#                 if longer_list[i] + longer_list[j] >= 10:
#                     l3[k] = longer_list[i] + longer_list[j] - 10
#                     l3[k - 1] += 1
#             else:
#                 l3[k] += longer_list[i]
#
# # 리스트를 출력합니다.
# print(l3)








