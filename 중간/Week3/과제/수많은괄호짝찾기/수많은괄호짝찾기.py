# import sys
# sys.stdin = open('input.txt', 'r')
#
# for tc in range(1,11):
#     howmany= int(input())
#     Data= input()
#     ans = 0
#     stack = []
#
#     for i in range(howmany):
#         if Data[i] in '([{<':
#             stack.append(Data[i])
#         elif stack and (Data[i]==')' and stack[-1]=='(') or (Data[i]=='}' and stack[-1]=='{') and (Data[i]==']' and stack[-1]=='[') and (Data[i]=='>' and stack[-1]=='<'):
#             stack.pop()
#         else: break
#
#     if not stack : ans = 1
#
#     print(f"#{tc} {ans}")

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    howmany = int(input()) #input 파일 내에 있는 순서번호 읽어옴(int형)
    Data = input() #괄호 대기열 읽어들임
    ans = 0
    stack = []

    for i in range(howmany):
        char = Data[i]

        if char in '([{<':
            stack.append(char) #여는 괄호일 경우 스택에 추가
        elif char in ')]}>': #닫는 괄호 기호일 경우
            if not stack: #stack=[]이므로 빈 배열일 경우를 묻는다
                break #stack 배열이 비어있지 않은 경우 멈춤(괄호쌍이 맞지 않으므로)
            top = stack.pop() #맨 위에 있는 기호 꺼내오기(top이라는 변수로 저장)
            if (char == ')' and top == '(') or (char == '}' and top == '{') or (char == ']' and top == '[') or (char == '>' and top == '<'):
                continue #괄호쌍이 맞으면 위 elif 부분 다시 돌기
            else:
                break
    else:
        if not stack: #위에서 스택이 비어있지 않은 경우
            ans = 1

    print(f"#{tc} {ans}")

