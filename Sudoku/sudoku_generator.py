import random
from sudoku import Sudoku

class SudokuGenerator :
    def __init__(self):
        self.sudoku = Sudoku()
 
    def _empty_cells(self,count):
        #making sure that are filled cells
        if count > 60 :
            count = 60
        for _ in range(count):
            self.sudoku.set_value(random.randint(0,8),random.randint(0,8),0)


    def _generate_full_sudoku(self):
        for i in range (self.sudoku.row_size):
            for j in range(self.sudoku.column_size):
                #if there is empty cell, sudoku not complete, we fill it 
                if self.sudoku.get_value(i,j) == 0:
                    validNumbers = list(range(1, 10))
                    random.shuffle(validNumbers)
                    #we get a random number from 1 to 9
                    for val in validNumbers:
                        #we check if we can enter the value in the cell
                        if self.sudoku.isValuePossible(i,j,val):
                            #if true, we enter the value in the cell
                            self.sudoku.set_value(i,j,val)
                            #we recursively call the function to find the next empty cell and fill it / or end the sudoku if complete
                            if self._generate_full_sudoku():
                                return True
                            #if filling the sudoku fails , reset the cell and try next number
                            self.sudoku.set_value(i,j,0)
                    #if no value is possible, return False
                    return False
        #if no empty cell is found, the sudoku is complete
        return True
    
    def generate_sudoku(self):
        self._generate_full_sudoku()
<<<<<<< HEAD
        self._empty_cells(40)
=======
        self.empty_cells(40)
>>>>>>> 3842bd173eaaf63d9e476a9b81eb6e696383e79c
        return self.sudoku




if __name__ == "__main__":
    sudoku_generator = SudokuGenerator()
    sudoku = sudoku_generator.generate_sudoku()
    sudoku.print_sudoku()
