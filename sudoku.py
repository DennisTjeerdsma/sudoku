class Cell(object):
    def __init__(self, row, column, editable=True, value=0, size=9):
        """
        The cell class holds the attributes of 1 unit cell of Sudoku. The cells has the following attributes:
        - Row index from 0-8 holding the row from top to bottom
        - Column index from 0-8 holding thhe columns from left to right
        - Editable parameter specifying if the current cells value is permanent or fluent
        - Value, the value currently stored in the cell from 0-9, 0 indicating no current value being held
        - Possible Values, a set of possible values for the cell based on the regions a cell occupies
        """
        self._row:int = row                  # The row of the cell object, rows can have a value of 0 - 8
        self._column: int = column           # The column of the cell object, columns can have a value of 0-8
        self._editable = editable            # Editable property of the cell, if editable is true, the value can be adjusted
        self._value: int = value             # The value of the object cell
        self._possibleValues = set(range(1, size + 1)) if self._editable is False else set()

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
        elif v == 0:
            self._value = v
        else: 
            self._value = v
            self.clear_possible_values()

    def clear_possible_values(self):
        """
        Function clearing the possible values from a set, returning a new empty set
        Used when value of the cell is permanent
        """
        self._possibleValues = set()

    def remove_possible_value(self, value: int):
        """
        Removes a value from a set if the value is present in the current set
        """
        if value in self._possibleValues:
            self._possibleValues.remove(value)

    @property
    def editable(self) -> bool:
        """ Return a boolean value based on if the cell is editable"""
        return self._editable

    @editable.setter
    def editable(self, e) -> bool:
        self._editable = e

    def intersect_possible_values(self, values):
        """
        Function intersecting the possible values from the region with the set held by the cell 
        The intersect function takes the elements in both sets and return a set for corresponding values in the sets
        """
        self._possibleValues = self._possibleValues.intersection(values)

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
    
    def get_cell(self, c):
        return self._cells[c]

    def update_cells_values(self):
        """
        Function updating all possible values of all cells in a region. 
        Creates a set of numbers from 1 to 9 and checks if numbers are taken in the regions by moving through the cell values
        Taken values are removed from the set. Update possible values will be called for all of the regions a cell belongs to
        The possible values are stored inside the cell. 
        """
        values_set = set(range(1, 1+len(self._cells)))
        
        # For-loop generating the possible values for the blank cells based on the current region
        for cell in self._cells:
            cell_value = cell.value
            if cell_value in values_set:
                values.remove(cell_value)
        
        cell.intersect_possible_values(values_set)
    
    def remove_possible_value_cell_region(self, cell: Cell, value: int):
        """
        Remove a value from a cells set of possible values if the cell is in the region
        - Cell, to check if the cell is in the current region
        - Value, the to be removed value from every cell in the current region
        """
        if cell in self._cells:
            for cell in self._cells:
                cell.remove_possible_value(value)
    
    def is_solved(self) -> bool:
        """
        Function checking if the current region is solved. A region is solved if all values have a non-zero value 
        in range(1, number of cells in region)
        """

        values_in_region = set()
        for cell in self_cells:
            values_in_region.add(cell.value)
        
        return values_in_region == set(1, len(self._cells) + 1)


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
        self._size = int(len(self._puzzle))
        self._regions = [Region() for _ in range(0, 3*self._size)]
        self._boxSize = int(self._size ** .5)

    @property
    def puzzle(self):
        return self._puzzle

    @property
    def regions(self):
        return self._regions

    def initialize_board(self):
        """
        Generate the cells for the board. Rows and columns are populated first, the cells are extracted and entered into the box regions
        """
        for r_i, row in enumerate(self._puzzle):
            for c_i, column in enumerate(row):
                temp_cell = Cell(r_i, c_i, False if column == 0 else True , column)
                self._regions[r_i].add_cell(temp_cell)
                self._regions[self._size + c_i].add_cell(temp_cell)
        
        # Populates the box regions with the previously generated cells
        box_region = self._size * 2
        
        for x_start in range(self._boxSize):
            for y_start in range(self._boxSize):
                for x in range(x_start * self._boxSize, (x_start + 1) * self._boxSize):
                    for y in range(y_start * self._boxSize, (y_start + 1) * self._boxSize):
                        self._regions[box_region].add_cell(self._regions[x].cells[y])
                box_region += 1
    
    def update_all_cells(self):
        for region in self._regions:
            region.update_cells_values()

    def solve(self):
        self.initialize_board()

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

class BruteForce(object):
    

if __name__ == '__main__':
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
    sudoku.solve()

