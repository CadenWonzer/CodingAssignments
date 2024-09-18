"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Caden Wonzer and Isabella Chojnacki, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: czw99
UT EID 2: ilc422
"""


# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def row_major_traversal(grid):
    """Traverses the grid row by row"""
    order = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pair = (i,j)
            order.append(pair)
    return order

# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def column_major_traversal(grid):
    """Traverses the grid column by column"""
    order = []
    col_len = len(grid[0])
    for j in range(col_len):
        for i in range(len(grid)):
            pair = (i, j)
            order.append(pair)
    return order


# Iterates over a 2D list from top to bottom then left to right
# and returning the coordinates (row, column).
def row_zigzag_traversal(grid):
    """Traveres the grid row by row in a zig-zag right left order"""
    order = []
    for i in range(len(grid)):
        if i % 2 == 0:
            for j in range(len(grid[i])):
                pair = (i, j)
                order.append(pair)
        if i % 2 == 1:
            for j in range(len(grid[i])-1, -1, -1):
                pair = (i, j)
                order.append(pair)
    return order


# Iterates over a 2D list by alternating between iterating
# left to right and right to left, going from top to bottom
# and returning the coordinates (row, column).
def column_zigzag_traversal(grid):
    """Travereses the grip in column by column in a zig-zag top to bottom order"""
    order = []
    col_len = len(grid[0])
    for j in range(col_len):
        if j % 2 == 0:
            for i in range(len(grid)):
                pair = (i, j)
                order.append(pair)
        if j % 2 == 1:
            for i in range(len(grid)-1, -1, -1):
                pair = (i, j)
                order.append(pair)
    return order


# Iterates over a 2D list from the top-right to the bottom-left
# in the direction of the main diagonal and returning the
# coordinates (row, column).
def main_diagonal_traversal(grid):
    """Traverses the grid in diagons from top right to bottom left"""
    order = []
    for j in range(len(grid[0])-1, -1, -1):
        pair = (0, j)
        order.append(pair)
        num = 1
        while num < len(grid) and j+num < len(grid[0]):
            pair = (num, j+num)
            order.append(pair)
            num+=1
    for i in range(1, len(grid), 1):
        pair = (i, 0)
        order.append(pair)
        num = 1
        while i+num < len(grid) and num < len(grid[0]):
            pair = (i+num, num)
            order.append(pair)
            num+=1
    return order

# Iterates over a 2D list from the top-left to the bottom-right
# in the direction of the secondary diagonal and returning the
# coordinates (row, column).
def secondary_diagonal_traversal(grid):
    """Traverses the grid in diagons from top left to bottom right"""
    order = []
    for j in range(0, len(grid[0]), 1):
        pair = (0, j)
        order.append(pair)
        num = 1
        while num < len(grid) and j-num > -1:
            pair = (num, j-num)
            order.append(pair)
            num+=1
    for i in range(1, len(grid), 1):
        pair = (i, len(grid[0])-1)
        order.append(pair)
        num = 1
        while i+num < len(grid) and len(grid[0])-1-num > -1:
            pair = (i+num, len(grid[0])-1-num)
            order.append(pair)
            num+=1
    return order


# Iterates over a 2D list in spiral order and returning the
# coordinates (row, column).
def spiral_traversal(grid):
    """Traverses grip in a spiral starting from the top left"""
    order = []
    top_offset = 1
    bottom_offset = 0
    left_offset = 0
    right_offset = 0
    end_size = len(grid) * len(grid[0])
    turn = 1
    for j in range(len(grid[0])):
        pair = (0, j)
        order.append(pair)
    while len(order) < end_size:
        if turn % 2 == 0:
            if turn % 4 == 2:
                for j in range(len(grid[0])-1-right_offset, left_offset-1, -1):
                    pair = (len(grid)-1-bottom_offset, j)
                    order.append(pair)
                bottom_offset+=1
            else:
                for j in range(left_offset, len(grid[0])-right_offset, 1):
                    pair = (top_offset, j)
                    order.append(pair)
                top_offset+=1
        if turn % 2 == 1:
            if turn % 4 == 3:
                for i in range(len(grid)-1-bottom_offset, top_offset-1, -1):
                    pair = (i, left_offset)
                    order.append(pair)
                left_offset+=1
            else:
                for i in range(top_offset, len(grid)-bottom_offset, 1):
                    pair = (i, len(grid[0])-1-right_offset)
                    order.append(pair)
                right_offset+=1
        turn+=1
    return order
