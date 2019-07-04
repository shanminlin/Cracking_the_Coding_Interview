"""
Chapter 1 - Problem 1.8 - Zero Matrix
Problem:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Solution:
1. Clarify the question:
Rephrase the question: We are given a matrix with dimension M by N. And When one element is 0, we need to set all rows
                       and columns of that element to 0.
Clarify assumptions: - Do we modify the matrix in place or return a new matrix? (We will modify the matrix in place.)
                     - The dimension of the matrix can be both square and non-square? (Yes)

2. Inputs and outputs:
So we are taking in a matrix with dimension M x N, and returning the matrix where when a 0 is seen, its entire row and
column are set to 0.

3. Test and edge cases:
edge: So we can also take in an empty matrix or a none object.
test:  We can also have regular input like this: [1,0,3,       [0,0,0,
                                                  0,5,6,   ->   0,0,0,
                                                  7,8,9]        0,0,3]

4. Brainstorm solution
we can iterate through the entire matrix, whenever we find a zero, we store its row and column number using two arrays.
Then we iterate through the array, for each row/column that is zero, set the whole row/column to be zero.
We are using extra spaces to store the row and column number. So space complexity is O(M+N).

To improve on this and further reduce space complexity, we can try to use the matrix itself to store the row and column
numbers that need to be set to zero. For example, we can use the first row to store the column number and the first column
to store the row number. As this will modify the values in the first row and column, we need two additional variables to note
whether the original first row and column need to be zeroed. So the space complexity is constant O(1)


5. Runtime analysis:
Time complexity: O(MxN) in always case as we need to iterate through the whole matrix.
Space complexity: O(1) in always case for the optimal solution

6. Code
"""


# Solution 1
# space complexity: O(M+N)
def zero_matrix1(matrix):

    if (matrix == [[]]) or (matrix is None):
        return matrix

    n_row = len(matrix)
    n_col = len(matrix[0])

    zero_rows = []
    zero_cols = []
    for i in range(n_row):
        for j in range(n_col):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)

    for row in zero_rows:
        for j in range(n_col):
            matrix[row][j] = 0

    for col in zero_cols:
        for i in range(n_row):
            matrix[i][col] = 0

    return matrix


# Solution 2
# Space complexity: O(1)
def zero_matrix2(matrix):
    if (matrix == [[]]) or (matrix is None):
        return matrix

    n_row = len(matrix)
    n_col = len(matrix[0])

    # check if first row and column contain zero
    first_row = False
    first_col = False
    for i in range(n_row):
        if matrix[i][0] == 0:
            first_col = True
            break

    for j in range(n_col):
        if matrix[0][j] == 0:
            first_row = True
            break

    # check the whole matrix for zero, and store result in first row and column
    for i in range(1, n_row):
        for j in range(1, n_col):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # zero out matrix based on values stored in first row and column
    for j in range(1, n_col):
        if matrix[0][j] == 0:
            for i in range(1, n_row):
                matrix[i][j] = 0

    for i in range(1, n_row):
        if matrix[i][0] == 0:
            for j in range(1, n_col):
                matrix[i][j] = 0

    # check original first row and column
    if first_row:
        for j in range(n_col):
            matrix[0][j] = 0
    if first_col:
        for i in range(n_row):
            matrix[i][0] = 0

    return matrix


# 7 Test and debug
assert zero_matrix1([[1, 0, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 0, 12]]
assert zero_matrix2([[1, 0, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 0, 12]]
assert zero_matrix1([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]
assert zero_matrix2([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]
assert zero_matrix1([[]]) == [[]]
assert zero_matrix2([[]]) == [[]]
assert zero_matrix1(None) is None
assert zero_matrix2(None) is None


