def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(A, n):
    result = A
    for _ in range(n - 1):
        result = matrix_multiply(result, A)
    
    return result
# Example graph 
graph = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
]

# Calculate paths of length 2 in the given graph
path_length = 2
result_matrix = matrix_power(graph, path_length)

print(f"Number of paths of length {path_length} between vertices:")
for row in result_matrix:
    print(row)
