import sys
from mpi4py import MPI
import numpy as np

def parallel_multiply_matrices_mpi(matrix1, matrix2):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Basic dimension check (can be made more robust)
    if len(matrix1[0]) != len(matrix2):
        if rank == 0:
            print("Error: Number of columns in the first matrix must equal the number of rows in the second matrix.")
        return None

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Only the root process handles the initial data and gathers results
    if rank == 0:
        matrix_a = np.array(matrix1)
        matrix_b = np.array(matrix2)
        result_matrix = np.empty((rows1, cols2), dtype=int)

        # Distribute rows of matrix_a to other processes
        rows_per_process = rows1 // size
        remainder = rows1 % size

        for i in range(size):
            start_row = i * rows_per_process + min(i, remainder)
            end_row = start_row + rows_per_process + (1 if i < remainder else 0)
            if i == 0:
                # The root process works on its assigned rows
                local_matrix_a = matrix_a[start_row:end_row, :]
            else:
                # Send rows to other processes
                comm.send(matrix_a[start_row:end_row, :], dest=i, tag=11)
                # Send matrix_b to other processes
                comm.send(matrix_b, dest=i, tag=22)

    else:
        # Receive rows of matrix_a and matrix_b
        local_matrix_a = comm.recv(source=0, tag=11)
        matrix_b = comm.recv(source=0, tag=22)
        result_matrix = None # Only root process holds the final result array

    # Each process performs multiplication on its assigned rows
    if local_matrix_a is not None:
        local_result = np.dot(local_matrix_a, matrix_b)
    else:
        local_result = None

    # Gather results from all processes to the root
    comm.Gather(local_result, result_matrix, root=0)

    if rank == 0:
        return result_matrix
    else:
        return None


if __name__ == "__main__":
    # Check if there are enough command-line arguments
    if len(sys.argv) == 3:
        # The script name is sys.argv[0], so arguments start from index 1
        #matrix_a = sys.argv[1]
        #matrix_b = sys.argv[2]
        matrix_a = np.load(sys.argv[1])
        matrix_b = np.load(sys.argv[2])
        product = parallel_multiply_matrices_mpi(matrix_a, matrix_b)
        if MPI.COMM_WORLD.Get_rank() == 0 and product is not None:
            print(f"Rank: {MPI.COMM_WORLD.Get_rank()}, shape: {product.shape}")
    else:
        print("Usage: python3 script.py matrix_a matrix_b")
