import sys
sys.stdin = open('input.txt','r')
abcChocolate = "abcabc"

T = int(input())
for i in range(T):
    wordlist = []
    len = int(input())
    word = str(input())
    wordlist.append(word)
    print(wordlist)
    for k in range(1, 7):
        if wordlist[i] * k == abcChocolate:
            result = "Yes"
        else:
            result = "No"
        print(f"#{i+1} {result}")


