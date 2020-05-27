class Cell(object):
    def __init__(self, row, column, editable=True, value=0):
        self.row:int = row               # The row of the cell object, rows can have a value of 0 - 8
        self.column: int = column           # The column of the cell object, columns can have a value of 0-8
        self.editable = editable            # Editable property of the cell, if editable is true, the value can be adjusted
        self.value: int = value             # The value of the object cell
        self.possibleValues = set()

    @property
    def row(self) -> int:
        # property of cell retrieving the private _row index of the cell instance
        return self._row

    @row.setter
    def row(self, r) -> int:
        # property of cell setting the private _row index of the cell instance, value must be between 0 - 8, hard coded for 9x9 sudoku
        if (r < 0 or r > 8): raise ValueError("Row value must be a value of 0 or higher or 8 or lower")
        self._row = r

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, c) -> int:
        # property of cell setting the private _column index of the cell instance, value must be between 0 - 8, hard coded for 9x9 sudoku
        if (c < 0 or c > 8): raise ValueError("Column value must be a value of 0 or higher or 8 or lower ")
        self._column = c

    @property
    def value(self) -> int:
        # propery of cell return the value variable
        return self._value

    @value.setter
    def value(self, v) -> int:
        # Value setter of the cell class, throws an error if the cell is not editable or if the value is not from 1 to 9
        if self.editable is False and v != 0:
            raise AttributeError("Cell is not editable")
        elif v < 0 or v > 9:
            raise ValueError(f"Incorrect value {v} not between or equal to <1,9>")
        else: self._value = v

    @property
    def editable(self) -> bool:
        """ Return a boolean value based on if the cell is editable"""
        return self._editable

    @editable.setter
    def editable(self, e) -> bool:
        self._editable = e

class Region(object):
    """
    Class holding a list of cells that have unique values. Can be a:
    - row
    - column
    - box
    The type of the class is not nexecarry
    """
    def __init__(self):
        self._cells = []

    @property
    def cells(self):
        return self._cells

class Sudoku(object):
    """
    Class holding the sudoku game object. 
    Cells are generated based on the 2d input puzzle.
    """
    def __init__(self, puzzle):
        self._puzzle = puzzle# Value holding a 2d array of the to be solved puzzle
        self._cells = []
    
    @property
    def puzzle(self):
        return self._puzzle

class SudokuSerializer(object):
    """
    Sudoku initializer takes an input of a sudoku board and turns it into a 2d array for the sudoku class
    For now, sudoku initializer only takes a 2d string as input, in the future arrays and 1d string will be incldued
    """
    @staticmethod
    def create_from_string(puzzle):
        if isinstance(puzzle, str):
            l = []
            for row in puzzle.split():
                row_arr = [int(i) for i in row]
                l.append(row_arr)
            return Sudoku(l)

if __name__ == '__main__':
    cell = Cell(8,4, False, 0)
    
    sudoku_string = """
                    500009100
                    000062508
                    010008764
                    065013020
                    240007010
                    000000000
                    070000056
                    058700300
                    000040800         
                    """
    print("TEST")

    sudoku = SudokuSerializer.create_from_string(sudoku_string)
      
