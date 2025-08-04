# Define matrix A (m x n)
A = [[1, 2],
     [3, 4],
     [5, 6]]

# Define matrix B (n x p)
B = [[7, 8, 9],
     [10, 11, 12]]

# Matrix multiplication: result will be m x p
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

# Multiply A and B
for i in range(len(A)):              
    for j in range(len(B[0])):       
        for k in range(len(B)):    
            result[i][j] += A[i][k] * B[k][j]

# Print result
print("Matrix A x Matrix B =")
for row in result:
    print(row)
