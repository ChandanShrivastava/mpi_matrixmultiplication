start_time = time.time()

!mpirun --allow-run-as-root --oversubscribe -np 2 python multiplymatrics_mpi.py matrix_a matrix_b

# Stop the timer
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

print(f"Execution time for a MPI run: {execution_time:.6f} seconds")