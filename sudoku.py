class Cell(object):
    def __init__(self, row, column, editable=True, value=0):
        """
        The cell class holds the attributes of 1 unit cell of Sudoku. The cells has the following attributes:
        - Row index from 0-8 holding the row from top to bottom
        - Column index from 0-8 holding thhe columns from left to right
        - Editable parameter specifying if the current cells value is permanent or fluent
        - Value, the value currently stored in the cell from 0-9, 0 indicating no current value being held
        - Possible Values, a set of possible values for the cell based on the regions a cell occupies
        """
        self._row:int = row               # The row of the cell object, rows can have a value of 0 - 8
        self._column: int = column           # The column of the cell object, columns can have a value of 0-8
        self._editable = editable            # Editable property of the cell, if editable is true, the value can be adjusted
        self._value: int = value             # The value of the object cell
        self._possibleValues = set()

    @property
    def row(self) -> int:
        # property of cell retrieving the row index of the cell instance
        return self._row

    @row.setter
    def row(self, r) -> int:
        # property of cell setting the row index of the cell instance, value must be between 0 - 8, hard coded for 9x9 sudoku
        if (r < 0 or r > 8): raise ValueError("Row value must be a value of 0 or higher or 8 or lower")
        self._row = r

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, c) -> int:
        # property of cell setting the column index of the cell instance, value must be between 0 - 8, hard coded for 9x9 sudoku
        if (c < 0 or c > 8): raise ValueError("Column value must be a value of 0 or higher or 8 or lower ")
        self._column = c

    @property
    def value(self) -> int:
        # propery of cell return the value variable
        return self._value

    @value.setter
    def value(self, v) -> int:
        # Value setter of the cell class, throws an error if the cell is not editable or if the value is not from 1 to 9
        if self.editable is False and v!= 0:
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
        self._cells = []    # initializes empty private array variable for Region to hold cells in
        
    def add_cell(self, cell: Cell):
        """
        Function adding cell to the region, check if cell is already in list 
        """
        if not cell in self._cells:
            self._cells.append(cell)

    @property
    def cells(self):
        return self._cells  
        
class Sudoku(object):
    """
    Class holding the sudoku game object. 
    Cells are generated based on the 2d input puzzle.
    #
    Attributes:
    - Puzzle, hold a 2d array of the actual sudoku puzzle. 0's indicate empty fields
    - Cells, holds the cell objects in the current puzzle
    #
    """
    def __init__(self, puzzle):
        self._puzzle = puzzle# Value holding a 2d array of the to be solved puzzle
        self._regions = [Region() for x in range(0, 27)]

        reg = 0

        for row in range(0, 9):
            for column in range(0, 9):
                self._regions[row].add_cell(Cell(row, column, self._puzzle[row][column]))
                self._regions[row+column].add_cell(Cell(row, column, self._puzzle[row][column])) 
            reg += 1
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

    sudoku = SudokuSerializer.create_from_string(sudoku_string)