# BabyGinNumbers = input("6자리 숫자를 입력하세요: ")
# nums = str(BabyGinNumbers)
#
# BabyGin = []
#
# # if len(nums) == 6:
# #     for i in range(5):
# #         if nums[i] in '1234567890':
# #             if nums[i].count >= 3:
# #                 print("Baby-Gin!!")
#
# def Triplet(inputNum):
#
#
#
# def Run():
#
#
#
# else:
#     print("6자리 숫자를 입력해 bitch")
#
#     #if Password[j] in '1234567890':

def is_run(cards):
    cards.sort()
    return (cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2]) or (cards[3] + 1 == cards[4] and cards[4] + 1 == cards[5])

def is_triplet(cards):
    return cards[0] == cards[1] and cards[1] == cards[2] or cards[3] == cards[4] and cards[4] == cards[5]

def is_babygin(cards):
    if is_run(cards) or is_triplet(cards):
        return True
    return False

# 예시로 실행
user_cards = [1, 2, 3, 4, 5, 6]
if is_run(user_cards):
    print("Run입니다.")
if is_triplet(user_cards):
    print("Triplet입니다.")
if is_babygin(user_cards):
    print("Baby-gin입니다.")




