# Importing random
import random
from array import *

# Adding base numbers
numbers = [1,2,3,4]

# Setting up the base board
board = [[0],[0],[0],[0]]

# Shuffling numbers for the first row
numbers_shuffled = random.sample(numbers, len(numbers))
for i in range(len(numbers_shuffled)):
    board[0].append(numbers_shuffled[i])
board[0].remove(0)
row_1 = board[0]

# First square
unavailable_numbers = [board[0][0],board[0][1]]
numbers_temp = [1,2,3,4]
for i in range(len(unavailable_numbers)):
    pop = unavailable_numbers[i]
    numbers_temp.remove(pop)
numbers_temp = random.sample(numbers_temp,len(numbers_temp))
for i in range(len(numbers_temp)):
    board[1].append(numbers_temp[i])
board[1].remove(0)

# Second square
unavailable_numbers = random.sample(unavailable_numbers, len(unavailable_numbers))
for i in range(len(unavailable_numbers)):
    board[1].append(unavailable_numbers[i])

# First column
unavailable_numbers = [board[0][0],board[1][0]]
numbers_temp = [1,2,3,4]
for i in range(len(unavailable_numbers)):
    pop = unavailable_numbers[i]
    numbers_temp.remove(pop)
numbers_temp = random.sample(numbers_temp, len(numbers_temp))
for i in range(len(numbers_temp)):
    board[i+2].append(numbers_temp[i])
    board[i+2].remove(0)

# Second Column
unavailable_numbers = random.sample(unavailable_numbers, len(unavailable_numbers))
for i in range(len(unavailable_numbers)):
    board[i+2].append(unavailable_numbers[i])

# C,3
unavailable_numbers = [1,2,4]
temp = [1,3]
numbers_temp = []
# temp = [board[0][2],board[1][2],board[2][0],board[2][1]]
print(temp)
passed = True
for i in range(len(temp)):
    for r in range(len(unavailable_numbers)):
        if unavailable_numbers[r] == temp[i]:
            passed = False
    if passed == True:
        numbers_temp.append(temp[i])
    passed = False
print(numbers_temp)

# print(board[0])
# print(board[1])
# print(board[2])
# print(board[3])