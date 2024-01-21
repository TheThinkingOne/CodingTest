# import sys
# sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때
#
# T = int(input())
# for tc in range(1,T+1):
#     postFix = list(input().split())
#     stack = []
#     print("%d " %tc, end = '')
#
#     for now in postFix:
#         if now.isdigit():
#             stack.append(int(now))
#         elif now == '.':
#             if len(stack) != 1 : print('Error!')
#             print(stack[0])
#         else:
#             if now in ('+','-','*','/'):
#                 if len(stack) < 2 :
#                     print('Error!')
#                     break
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 if now == '*':
#                     temp=num1*num2
#                     stack.append(temp)
#                 elif now == '/':
#                     temp = num1 / num2
#                     stack.append(temp)
#                 elif now == '+':
#                     temp = num1 + num2
#                     stack.append(temp)
#                 elif now == '-':
#                     temp = num1 - num2
#                     stack.append(temp)
#4주차 문제인 철수비밀번호 풀어보기

##gpt물어봐서 나온 온전한 코드

import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때

t = int(input())

for i in range(t):
    nlist = input().split()
    stack = []
    print("#%d" % (i + 1), end=" ")

    for j in nlist:
        if j.isdigit():  # 숫자인 경우
            stack.append(int(j))
        elif j == ".":  # 결과 출력
            if len(stack) == 1:
                print(stack.pop())
            else:
                print("error")
                break
        else:  # 연산자인 경우
            if len(stack) >= 2:
                n2 = stack.pop()
                n1 = stack.pop()
                if j == "+":
                    n3 = n1 + n2
                elif j == "-":
                    n3 = n1 - n2
                elif j == "*":
                    n3 = n1 * n2
                elif j == "/":  # 나눗셈 연산 추가
                    if n2 == 0:
                        print("error")
                        break
                    n3 = n1 // n2
                else:
                    print("error")
                    break
                stack.append(n3)
            else:
                print("error")
                break