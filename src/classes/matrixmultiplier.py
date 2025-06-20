import numpy as np

class MatrixMultiplier:
    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        # Get dimensions
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])

        # Check if multiplication is possible
        if cols1 != rows2:
            return "Error: Number of columns in the first matrix must equal the number of rows in the second matrix."

        # Initialize result matrix with zeros
        result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]
        # Perform multiplication
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return result_matrix
    
    def create_squarematrix(length):
        matrix = np.random.randint(0, 1000, size=(length, length)).tolist()
        for row in matrix:
            print(row)
        return matrix