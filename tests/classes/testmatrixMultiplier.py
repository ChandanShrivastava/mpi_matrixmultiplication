import unittest
from src.classes.matrixmultiplier import MatrixMultiplier

class TestMatrixMultiplier(unittest.TestCase):

    def test_valid_multiplication(self):
        matrix1 = [
            [1, 2],
            [3, 4]
        ]
        matrix2 = [
            [5, 6],
            [7, 8]
        ]
        expected = [
            [19, 22],
            [43, 50]
        ]
        result = MatrixMultiplier.multiply_matrices(matrix1, matrix2)
        self.assertEqual(result, expected)
    
    def test_valid_multiplication2(self):
        matrix1 = MatrixMultiplier.create_squarematrix(2)
        matrix2 = MatrixMultiplier.create_squarematrix(2)
 
        result = MatrixMultiplier.multiply_matrices(matrix1, matrix2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(matrix1))

    def test_invalid_multiplication(self):
        matrix1 = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        matrix2 = [
            [7, 8],
            [9, 10]
        ]
        result = MatrixMultiplier.multiply_matrices(matrix1, matrix2)
        self.assertIsInstance(result, str)
        self.assertTrue("Error" in result)
        
    def test_square_matrix_creation(self):
        length = 3
        matrix = MatrixMultiplier.create_squarematrix(length)
        self.assertEqual(len(matrix), length)
        for row in matrix:
            self.assertEqual(len(row), length)
            for value in row:
                self.assertTrue(0 <= value < 1000)
    
    if __name__ == "__main__":
        unittest.main()