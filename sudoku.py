class Cell:
    def __init__(self, row, column, editable=True, value=0):
        self.value: int = value             # The value of the object cell
        self.row: int = row                 # The row of the cell object, rows can have a value of 0 - 8
        self.column: int = column           # The column of the cell object, columns can have a value of 0-8
        self._editable = editable            # Editable property of the cell, if editable is true, the value can be adjusted

    @property
    def row(self) -> int:
        return self._row

    @row.setter
    def row(self, r) -> int:
        if (r < 0 or r > 8): raise ValueError("Column value must be a value of 0 or higher or 8 or lower")
        self._row = r

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, c) -> int:
        if (c < 0 or c > 8): raise ValueError("Column value must be a value of 0 or higher or 8 or lower ")
        self._column = c

    @property
    def value(self) -> int:
        return self_value

    @value.setter
    def value(self, i) -> int:
        

