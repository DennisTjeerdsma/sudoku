import unittest

from sudoku import Cell as CellClass
from sudoku import Sudoku as SudokuClass
from sudoku import SudokuSerializer

class Test(unittest.TestCase):
    def setUp(self):
        self.cell1 = CellClass(4, 3, True, 1)
        self.cell2 = CellClass(3, 2, False, 4)
        self.sudoku1 = SudokuSerializer().create_from_string(
                    """
                    500009100
                    000062508
                    010008764
                    065013020
                    240007010
                    000000000
                    070000056
                    058700300
                    000040800         
                    """)
    def test_1_cell_exception_handling(self):
        self.assertRaises(ValueError, CellClass, 10, 4)
        self.assertRaises(ValueError, CellClass, -1, 3)
        self.assertRaises(ValueError, CellClass, 2, -1)
        self.assertRaises(ValueError, CellClass, 2, 9)

    def test_2_cell_value_assignment(self):
        self.assertEqual(self.cell1.row, 4)
        self.assertEqual(self.cell1.column, 3)
        self.assertEqual(self.cell1.value, 1)

    def test3_convert_sudoku_from_string_to_arr(self):
        self.assertEqual(self.sudoku1.puzzle, [[5,0,0,0,0,9,1,0,0],
                                                [0,0,0,0,6,2,5,0,8],
                                                [0,1,0,0,0,8,7,6,4],
                                                [0,6,5,0,1,3,0,2,0],
                                                [2,4,0,0,0,7,0,1,0],
                                                [0,0,0,0,0,0,0,0,0],
                                                [0,7,0,0,0,0,0,5,6],
                                                [0,5,8,7,0,0,3,0,0],
                                                [0,0,0,0,4,0,8,0,0]])

    def test4_assigning_cell_values(self):
        self.assertEqual(self.cell1.value, 1)
        self.assertTrue(self.cell1.editable)
        self.assertEqual(self.cell2.value, 4)
        self.assertFalse(self.cell2.editable)
        self.assertRaises(AttributeError, self.cell2.value, 2)
        self.assertEqual(self.cell1.value(5), 5)
        
if __name__ == '__main__':
    unittest.main()
    print("All tests passed")