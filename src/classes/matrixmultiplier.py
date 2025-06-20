import numpy as np
import sys

class MatrixMultiplier:
  
    def multiply_matrices(matrix1, matrix2):
        # Get dimensions
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])

        # Check if multiplication is possible
        if cols1 != rows2:
            print(rows1, cols1, rows2, cols2)
            return "Error: Number of columns in the first matrix must equal the number of rows in the second matrix."

        # Initialize result matrix with zeros
        result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]
        # Perform multiplication
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return np.array(result_matrix)
    
    def create_squarematrix(length):
        matrix = np.random.randint(0, 1000, size=(length, length)).tolist()
        print(f"Created matrix of row length: {len(matrix)}, cols: {len(matrix[0])}")
        return matrix


if __name__ == "__main__":
# Check if there are enough command-line arguments
    if len(sys.argv) == 3:
        # The script name is sys.argv[0], so arguments start from index 1
        matrix_a = np.load(sys.argv[1])
        matrix_b = np.load(sys.argv[2])
        product = MatrixMultiplier.multiply_matrices(matrix_a, matrix_b)
        print(product.shape)
    else:
        print("Usage: python3 script.py matrix_a matrix_b")