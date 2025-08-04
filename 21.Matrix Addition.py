# Input matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Initialize result matrix with zeros
result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

# Matrix addition using nested loops
for i in range(len(A)):           # rows
    for j in range(len(A[0])):    # columns
        result[i][j] = A[i][j] + B[i][j]

# Print result
print("Matrix A + Matrix B =")
for row in result:
    print(row)
