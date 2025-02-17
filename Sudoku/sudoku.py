class Sudoku:
    def __init__(self, matrix = None):
        self.row_size = 9
        self.column_size = 9
        
        if matrix is None:
            self.matrix = [[0 for i in range(9)] for _ in range(9)]
        else:
            if(len(matrix) != self.row_size or len(matrix[0]) != self.column_size):
                raise ValueError("Invalid matrix size")
            self.matrix = matrix

    def get_value(self, row, column):
        if 0<= row < self.row_size and 0<= column < self.column_size:
            return self.matrix[row][column]
        else:
            raise ValueError("Invalid row or column")
    
    def set_value(self, row, column, val):
        if 0<= row <= self.row_size and 0<= column <= self.column_size:
            self.matrix[row][column] = val
        else:
            raise ValueError("Invalid row or column")
        
    
    # def isValuePossible(self,x,y,val):
    #     #check if value is valid
    #     for i in range(self.row_size):
    #         #check same row
    #         if self.get_value(x,i) == val:
    #             return False
    #         #check same column
    #         if self.get_value(i,y) == val: 
    #             return False
    #         #check same 3x3 grid
    #         if self.get_value((x//3)*3 + i//3, ((y//3)*3 + i%3)) == val:
    #             return False
    #     return True
    
    def isValuePossible(self, row, column, val):
        for i in range(9):
            if self.matrix [row][i] == val or self.matrix [i][column] == val:
                return False
        start_row = row //3 * 3
        start_column = column //3 * 3
        for i in range(3):
            for j in range(3):
                if self.matrix[start_row + i][start_column + j] == val:
                    return False
        return True
    

    def print_sudoku(self):
        for i in range(self.row_size):
            for j in range(self.column_size):
                if(j % 3 == 2):
                    print(self.matrix[i][j], end=" | ")
                else:
                    print(self.matrix[i][j], end=" ")
            print()
            if(i % 3 == 2):
                print("----"*6)



if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.print_sudoku()
    print(sudoku.get_value(0,0))
    sudoku.set_value(0,0,5)
    print(sudoku.get_value(0,0))
    sudoku.print_sudoku()
    sudoku.set_value(7,7,5)
    sudoku.print_sudoku()