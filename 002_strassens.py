def strassen_matrix_multiply(A, B):
    n = len(A)

    # Base case: if matrices are 1x1, perform simple multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide matrices into submatrices
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Compute Strassen's algorithm matrices recursively
    P1 = strassen_matrix_multiply(A11, matrix_subtract(B12, B22))
    P2 = strassen_matrix_multiply(matrix_add(A11, A12), B22)
    P3 = strassen_matrix_multiply(matrix_add(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, matrix_subtract(B21, B11))
    P5 = strassen_matrix_multiply(matrix_add(A11, A22), matrix_add(B11, B22))
    P6 = strassen_matrix_multiply(matrix_subtract(A12, A22), matrix_add(B21, B22))
    P7 = strassen_matrix_multiply(matrix_subtract(A11, A21), matrix_add(B11, B12))

    # Compute the resulting submatrices
    C11 = matrix_add(matrix_subtract(matrix_add(P5, P4), P2), P6)
    C12 = matrix_add(P1, P2)
    C21 = matrix_add(P3, P4)
    C22 = matrix_subtract(matrix_subtract(matrix_add(P5, P1), P3), P7)

    # Combine submatrices to form the resulting matrix
    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])
    for i in range(mid):
        result.append(C21[i] + C22[i])
    return result

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example usage:
matrix_A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

result_matrix = strassen_matrix_multiply(matrix_A, matrix_B)
print("Resultant matrix:")
for row in result_matrix:
    print(row)
