"""
Chapter 1 - Problem 1.7 - Rotate Matrix
Problem:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

Solution:
1. Clarify the question:
Rephrase the question: We are given a matrix with dimension NxN. And we want to rotate the matrix by 90 degrees.
Clarify assumption: - clockwise or counterclockwise rotation? (We will assume clockwise rotation.)
                    - in place or not in place (For NxN matrix, we can do both.)
2. Inputs and outputs:
input: an NxN matrix
output: an NxN matrix but rotated 90 degrees

3. Test and edge cases:
edge: So we can also take in an empty matrix or none object as an input.
test: We can also have regular input like this: [1,2,3,       [7,4,1,
                                                 4,5,6,   ->   8,5,2,
                                                 7,8,9]        9,6,3]

4. Brainstorm solution:
Rows in the original matrix become columns. First row becomes last columns and so on. So we can first reverse the matrix
so that the first row becomes the last row, then transpose the matrix so that each row becomes a column.
[1,2,3,       [7,8,9,        [7,4,1,
 4,5,6,   ->   4,5,6  ->      8,5,2,
 7,8,9]        1,2,3]         9,6,3]

5. Runtime analysis:
Time complexity: O(N^2) in always-case as we need to perform operations on all cells of the matrix.
Space complexity: O(1) in always case as we only need to allocate enough space for one matrix cell.

6. Code
"""
def rotate_matrix(image):
    if (image is None) or (image == [[]]):
        return image
    # reverse the matrix
    image = image[::-1]

    # transpose the matrix as we iterate through each element
    n_row = len(image)
    n_col = len(image[0])

    for i in range(n_row):
        for j in range(i+1, n_col): # no swap for diagonal element (j=i) or repeat swap (j<i)
            temp = image[i][j]
            image[i][j] = image[j][i]
            image[j][i] = temp

    return image

# 7. Test and debug
assert rotate_matrix([[1,2,3], [4,5,6], [7,8,9]]) ==  [[7,4,1], [8,5,2], [9,6,3]]
assert rotate_matrix([[]]) == [[]]
assert rotate_matrix(None) is None







