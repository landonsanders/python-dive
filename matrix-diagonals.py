matrix = [
        [0, 1, 2, 3, 4],
        [3, 4, 5, 3, 4],
        [6, 7, 8, 3, 4],
        [6, 7, 8, 3, 4],
        [6, 7, 8, 3, 4]
        ]

def right_to_left_diagonal(matrix):
    count = 0
    for i, row in enumerate(matrix):
        i = len(row) - (i + 1)
        count = count + abs(row[i])
        
    return count
    
def left_to_right_diagonal(matrix):
    count = 0
    for i, row in enumerate(matrix):
        count = count + row[i]
        
    return count
    
menuend = left_to_right_diagonal(matrix)
subtrahend = right_to_left_diagonal(matrix)

print abs(menuend - subtrahend)