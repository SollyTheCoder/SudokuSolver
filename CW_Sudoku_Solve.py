## sudoku solver2
## input as list of rows
## eg sudoku([[5,3,0,0,7,0,0,0,0],
#             [6,0,0,1,9,5,0,0,0],
#             [0,9,8,0,0,0,0,6,0],
#             [8,0,0,0,6,0,0,0,3],
#             [4,0,0,8,0,3,0,0,1],
#             [7,0,0,0,2,0,0,0,6],
#             [0,6,0,0,0,0,2,8,0],
#             [0,0,0,4,1,9,0,0,5],
#             [0,0,0,0,8,0,0,7,9]])
              
def sudoku(puzzle):
    
    empty = find_empty(puzzle)
    if not empty:
        return puzzle
    else:
        row, col = empty

    for num in range(1,10):

        if valid(puzzle, num, row, col):
            puzzle[row][col] = num

            if sudoku(puzzle):
                return puzzle

            puzzle[row][col] = 0

    return False

    
    row, col = empty

    
    return empty



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] ==0:
                return (i, j)  ##row /column


def valid(board, number, row, col):
    ## column check
    for i in range(len(board)):
        if board[i][col] == number:
            return False

    ## row check

        if board[row][i] == number:
            return False

    # box check

    x_box = row // 3
    y_box = col // 3

    for i in range(3*x_box,3*x_box+3):
        for j in range(3*y_box,3*y_box+3):
            if board[i][j] == number and (i, j)!=(row, col):
                return False

    return True
    
    
