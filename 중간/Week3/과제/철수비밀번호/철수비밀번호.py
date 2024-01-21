import sys
sys.stdin = open('input.txt', 'r')

for i in range(10):
    TC, Password = map(int, input().split())
    Password = str(Password)
    stack = []
    for j in range(TC):
        if Password[j] in '1234567890':
            stack.append(Password[j])
    for k in range(TC):
        if (stack.count(k))%2 == 0:
            stack.remove(k)
        elif (stack.count(k))%2 == 1:
            stack.remove(k)
            stack.append(k)
    print(f"#{i+1} {stack}")

# import sys
#
# sys.stdin = open('input.txt', 'r')
#
# for i in range(10):
#     TC, Password = map(int, input().split())
#     Password = str(Password)
#     stack = []
#
#     for j in range(len(Password)):  # Password의 길이만큼 반복
#         if Password[j] in '1234567890':
#             num = Password[j]
#
#             # 스택이 비어있지 않고, 스택의 맨 위 숫자가 현재 숫자와 같으면 제거
#             if stack and stack[-1] == num:
#                 stack.pop()
#             else:
#                 stack.append(num)
#
#     result = ''.join(stack)
#
#     # 만약 결과가 빈 문자열인 경우 0을 출력
#     if not result:
#         result = '0'
#
#     print(f"#{i + 1} {result}")

# import sys
# sys.stdin = open('input.txt', 'r')
#
# for i in range(10):
#     TC, Password = map(int, input().split())
#     Password = str(Password)
#     stack = []
#     for j in range(TC):
#         if Password[j] in '1234567890':
#             stack.append(Password[j])
#     result_stack = []
#     for k in stack:
#         if result_stack and result_stack[-1] == k:
#             result_stack.pop()
#         else:
#             result_stack.append(k)
#     print(f"#{i + 1} {''.join(result_stack)}")









