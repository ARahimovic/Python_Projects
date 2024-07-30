import random

row_size = 9
column_size = 9

matrix = [[0 for i in range(9)] for _ in range(9)]


def isValueValid(x,y,val):
    #check if value is valid
    for i in range(9):
        #check same row
        if matrix[x][i] == val:
            return False
        #check same column
        if matrix[i][y] == val: 
            return False
        #check same 3x3 grid
        if matrix[(x//3)*3 + i//3][(y//3)*3 + i%3] == val:
            return False
    return True


def fillCompleteSudoku():
    for row in range(row_size):
        repeat_counter = 0
        column = 0
        while column < column_size:
            while repeat_counter < 9:
                    #generate random value
                    val = random.randint(1,9)
                    if (isValueValid(row,column,val)):
                    #if value is valid, I assign  it to the cell and move to the next column
                        matrix[row][column] = val
                        column += 1
                        repeat_counter = 0
                        break                    
                    else :    
                        #if value is not valid, I repeat the process and get another random value and check again
                        repeat_counter += 1
                        #if I have tried 9 times and still no valid value, I reset the row matrix and start again
                        if(repeat_counter >= 9):
                            #reset row matrix
                            matrix[row] = [0 for i in range(9)]
                            repeat_counter = 0
                            column = 0
                

def empty_cells(count):
    for x in range(count):
        i = random.randint(0,8)
        j = random.randint(0,8)
        matrix[i][j] = 0


def generate_sudoku():
    fillCompleteSudoku()
    empty_cells(40)
    return matrix

generate_sudoku()

def print_sudoku():
    for x in range(9):
        for y in range(9):
            if(y % 3 == 2):
                print(matrix[x][y], end=" | ")
            else:
                print(matrix[x][y], end=" ")
        print()
        if(x % 3 == 2):
            print("----"*6)

print_sudoku()
