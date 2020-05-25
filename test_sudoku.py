import unittest

from sudoku import Cell as CellClass

class Test(unittest.TestCase):
    def setUp(self):
        self.cell1 = CellClass(4, 3, True, 1)

    def test_1_cell_exception_handling(self):
        self.assertRaises(ValueError, CellClass, 9, 4)
        self.assertRaises(ValueError, CellClass, -1, 3)
        self.assertRaises(ValueError, CellClass, 2, -1)
        self.assertRaises(ValueError, CellClass, 2, 9)
        print("##-Correct Cell Exception handling-##\n")

    def test_2_cell_value_assignment(self):
        self.assertEqual(self.cell1.row, 4)
        self.assertEqual(self.cell1.column, 3)
        self.assertEqual(self.cell1.value, 1)
        print("##-Correct Row and column assignment-##")
        
if __name__ == '__main__':
    unittest.main()
    print("All tests passed")