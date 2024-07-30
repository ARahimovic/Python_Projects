from sudoku_generator import SudokuGenerator
from sudoku import Sudoku

class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
    
    def find_empty_location(self):
        for i in range(self.sudoku.row_size):
            for j in range(self.sudoku.column_size):
                if self.sudoku.get_value(i, j) == 0:
                    return i, j
        return None, None
    
    def solve(self):
        empty = self.find_empty_location()
        if empty == (None, None):
            return True
        row, column = empty
        for val in range(1,10):
            if self.sudoku.isValuePossible(row,column,val):
                self.sudoku.set_value(row, column , val)
                if self.solve():
                    return True
                self.sudoku.set_value(row, column, 0)
        return False
     


if __name__ == "__main__":
    # sudoku_generator = SudokuGenerator()
    # sudoku = sudoku_generator.generate_sudoku()
    # sudoku.print_sudoku()
    # print("time to solve it now")
    # sudoku_solver = SudokuSolver(sudoku)
    # sudoku_solver.solve()
    # sudoku.print_sudoku()

    #testing using a hardcoded sudoku
    new_puzzle = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]


    sudoku_hardcoded = Sudoku(new_puzzle)
    sudoku_hardcoded.print_sudoku()
    print("time to solve it now")
    sudoku_solver = SudokuSolver(sudoku_hardcoded)
    sudoku_solver.solve()
    sudoku_hardcoded.print_sudoku()