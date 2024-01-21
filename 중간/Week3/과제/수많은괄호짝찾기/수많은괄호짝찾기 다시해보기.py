import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    howmany = int(input()) #howmany는 괄호의 갯수 알려주는 숫자
    brackets = input()

    answer = 0
    House = []

    for i in range(howmany):
        char = brackets[i]

        if char in '({[<':
            House.append(char)
        elif char in ')}]>':
            if not House:
                break
            top = House.pop()
            if House and (brackets[i]==')' and brackets[-1]==')') or (brackets[i]=='}' and brackets[-1]=='}') or (brackets[i]==']' and brackets[-1]==']') or (brackets[i]=='>' and brackets[-1]=='}>'):
                continue
            else:
                break

    if not House:
        answer = 1
        print(f"{tc}, {answer}")