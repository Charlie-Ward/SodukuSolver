# Importing random
import random

# Adding base numbers
numbers = [1,2,3,4]

# Setting up the base board
board = []

numbers_shuffled = random.sample(numbers, len(numbers))
board.append(numbers_shuffled)
print(board)
row_1 = board[0]
print(row_1)