import sys
sys.stdin = open('input.txt', 'r')

sentence = list(map(str,input().split()))
print(len(sentence))