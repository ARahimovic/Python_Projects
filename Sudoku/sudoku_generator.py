import random
from sudoku import Sudoku

class SudokuGenerator :
    def __init__(self):
        self.sudoku = Sudoku()
 
    def empty_cells(self,count):
        #making sure that are filled cells
        if count > 60 :
            count = 60
        for _ in range(count):
            self.sudoku.set_value(random.randint(0,8),random.randint(0,8),0)
    
    # def isValuePossible(self,x,y,val):
    #     #check if value is valid
    #     for i in range(self.sudoku.row_size):
    #         #check same row
    #         if self.sudoku.get_value(x,i) == val:
    #             return False
    #         #check same column
    #         if self.sudoku.get_value(i,y) == val: 
    #             return False
    #         #check same 3x3 grid
    #         if self.sudoku.get_value((x//3)*3 + i//3, ((y//3)*3 + i%3)) == val:
    #             return False
    #     return True

    def generate_full_sudoku(self):
        for row in range(self.sudoku.row_size):
            repeat_counter = 0
            column = 0
            while column < self.sudoku.column_size:
                while repeat_counter < 9:
                        #generate random value
                        val = random.randint(1,9)
                        if (self.sudoku.isValuePossible(row,column,val)):
                        #if value is valid, I assign  it to the cell and move to the next column
                            self.sudoku.set_value(row, column, val)
                            column += 1
                            repeat_counter = 0
                            break                    
                        else :    
                            #if value is not valid, I repeat the process and get another random value and check again
                            repeat_counter += 1
                            #if I have tried 9 times and still no valid value, I reset the row matrix and start again
                            if(repeat_counter >= 9):
                                #reset row matrix
                                self.sudoku.matrix[row] = [0 for i in range(9)]
                                repeat_counter = 0
                                column = 0 
    
    def generate_sudoku(self):
        self.generate_full_sudoku()
        self.empty_cells(40)
        return self.sudoku




if __name__ == "__main__":
    sudoku_generator = SudokuGenerator()
    sudoku = sudoku_generator.generate_sudoku()
    sudoku.print_sudoku()
