# 1042. Toeplitz Matrix
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
# 样例
# Example 1:
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512
#
# In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
#
#
# Example 2:
#
# Input: matrix = [[1,2],[2,2]]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.


class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        if matrix == []:
            return True
        cow = len(matrix)
        if cow == 1 :
            return True
        row = len(matrix[0])
        for i in matrix:
            if len(i) != row:
                return False
        if row == 1 :
            return True
        min = row if row < cow else cow
        for i in range(cow):

            for j in range(min - i):

                # print(i,j)
                # print(matrix[i + j][0 + j])
                if matrix[i+j][0 + j] != matrix[i][0]:
                    return False
        for i in range(row):
            for j in range(min - i):
                if matrix[0+j][i + j] != matrix[0][i]:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    matrix = [
              [43,18,89,65,28,91,71,7,51,49,96,51,41,10,16,16],
              [5,43,18,89,65,28,91,71,7,51,49,96,51,41,10,16],
              [40,5,43,18,89,65,28,91,71,7,51,49,96,51,41,10],
              [57,40,5,43,18,89,65,28,91,71,7,51,49,96,51,41],
              [6,57,40,5,43,18,89,65,28,91,71,7,51,49,96,51],
              [39,6,57,40,5,43,18,89,65,28,91,71,7,51,49,96],
              [34,39,6,57,40,5,43,18,89,65,28,91,71,7,51,49],
              [80,34,39,6,57,40,5,43,18,89,65,28,91,71,7,51],
              [65,80,34,39,6,57,40,5,43,18,89,65,28,91,71,7],
              [29,65,80,34,39,6,57,40,5,43,18,89,65,28,91,71],
              [74,29,65,80,34,39,6,57,40,5,43,18,89,65,28,91],
              [31,74,29,65,80,34,39,6,57,40,5,43,18,89,65,28],
              [72,31,74,29,65,80,34,39,6,57,40,5,43,18,89,65],
              [53,72,31,74,29,65,80,34,39,6,57,40,5,43,18,89],
              [22,53,72,31,74,29,65,80,34,39,6,57,40,5,43,18],
              [54,22,53,72,31,74,29,65,80,34,39,6,57,40,5,43],
              [12,54,22,53,72,31,74,29,65,80,34,39,6,57,40,5],
              [16,12,54,22,53,72,31,74,29,65,80,34,39,6,57,40],
              [79,16,12,54,22,53,72,31,74,29,65,80,34,39,6,57],
              [35,79,16,12,54,22,53,72,31,74,29,65,80,34,39,6]]
    print(s.isToeplitzMatrix(matrix))





        # Write your code here
