# import sys
# sys.stdin = open('input.txt','r')
#
# T = int(input())
# for i in range(T):
#     j = int(input()) #j=3
#     V = []
#     E = []
#     for k in range(j): #k=0,1,2
#         result = ''
#         Data = input().split()
#         V.append(Data[0])
#         E.append(int(Data[1]))
#         if k < j-1:
#             if E[k] == 10:
#                 result = V[k]*E[k]
#             elif E[k] < 10:
#                 result = V[k]*E[k]+(V[k+1]*(10-E[k]))
#                 E[k+1] -= (10-E[k])
#         print(result)

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    j = int(input())
    V = []
    E = []
    result = ''
    line = ''
    for k in range(j):
        char, count = input().split()
        V.append(char)
        E.append(int(count))

    for k in range(j):
        while E[k] > 0:
            if len(line) < 10:
                append_count = min(E[k], 10 - len(line))
                line += V[k] * append_count
                E[k] -= append_count
            if len(line) == 10:
                result += line + '\n'
                line = ''

    if line:
        result += line

    print(f'#{i}')
    print(result)

# Read the input file lines
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#
# # Initialize the output list
# output = []
#
# # The first line is the number of test cases
# T = int(lines[0].strip())
#
# # Start reading the test cases
# line_number = 1  # Keeps track of the current line being read
#
# for _ in range(T):
#     # Number of character-number pairs for the current test case
#     j = int(lines[line_number].strip())
#     line_number += 1  # Move to the next line to start reading the pairs
#
#     # Lists to keep track of characters (V) and their counts (E)
#     V = []
#     E = []
#
#     # Read each pair for the current test case
#     for _ in range(j):
#         char, count = lines[line_number].split()
#         V.append(char)
#         E.append(int(count))
#         line_number += 1  # Move to the next line for the next pair
#
#     # Initialize the result string for the current test case
#     result = ''
#     line_length = 0  # Track the length of the current line
#
#     # Process the pairs
#     for k in range(j):
#         while E[k] > 0:
#             # Calculate the number of characters to append
#             append_count = min(E[k], 10 - line_length)
#             result += V[k] * append_count
#             line_length += append_count
#             E[k] -= append_count
#
#             # If we reach a line of 10 characters, reset the line length
#             if line_length == 10:
#                 result += '\n'
#                 line_length = 0
#
#     # Add the result of the current test case to the output list
#     output.append(result.strip())
#
# # The output list contains the processed strings for each test case
# for processed_string in output:
#     print(processed_string)



        # if E == 10:
        #     print(V*10)
        # elif E < 10:
        #     print(V*E, end='')
        #     print()

# import sys
#
# # Redirect the standard input to the file
# sys.stdin = open('input.txt', 'r')
#
# # Read the number of test cases
# T = int(input().strip())
#
# # Initialize the output list
# output = []
#
# for _ in range(T):
#     # Read the number of character-number pairs for the current test case
#     j = int(input().strip())
#
#     # Lists to keep track of characters (V) and their counts (E)
#     V = []
#     E = []
#
#     # Read each pair for the current test case
#     for _ in range(j):
#         char, count = input().split()
#         V.append(char)
#         E.append(int(count))
#
#     # Initialize the result string for the current test case
#     result = ''
#     line_length = 0  # Track the length of the current line
#
#     # Process the pairs
#     for k in range(j):
#         while E[k] > 0:
#             # Calculate the number of characters to append
#             append_count = min(E[k], 10 - line_length)
#             result += V[k] * append_count
#             line_length += append_count
#             E[k] -= append_count
#
#             # If we reach a line of 10 characters, reset the line length
#             if line_length == 10:
#                 result += '\n'
#                 line_length = 0
#
#     # Add the result of the current test case to the output list
#     output.append(result.strip())
#
# # The output list contains the processed strings for each test case
#     for processed_string in output:
#         print(f"#{_+1}")
#         print(processed_string)

# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input().strip())
#
# for i in range(1, T + 1):
#     j = int(input().strip())
#
#     V = []
#     E = []
#
#     for _ in range(j):
#         char, count = input().split()
#         V.append(char)
#         E.append(int(count))
#
#     # Print the test case number
#     print(f'#{i}')
#
#     # Initialize the result string for the current test case
#     result = ''
#     line_length = 0  # Track the length of the current line
#
#     # Process the pairs
#     for k in range(j):
#         while E[k] > 0:
#             # Calculate the number of characters to append
#             append_count = min(E[k], 10 - line_length)
#             result += V[k] * append_count
#             line_length += append_count
#             E[k] -= append_count
#
#             # If we reach a line of 10 characters, reset the line length
#             if line_length == 10:
#                 result += '\n'
#                 line_length = 0
#
#     print(result.strip(), end='\n\n')


