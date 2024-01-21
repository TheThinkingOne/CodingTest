import sys
sys.stdin = open('input.txt', 'r')

# word = list(str(input()))
# for i in range(len(word)):
#     asciiVal = ascii(word[i])
#     print(asciiVal)
word = str(input())

count = {}
for char in word:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        char_lower = char.lower()
        count[char_lower] = count.get(char_lower, 0) + 1

max_count = max(count.values())

max_chars = [char_upper for char_upper, char_count in count.items() if char_count == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0].upper())

