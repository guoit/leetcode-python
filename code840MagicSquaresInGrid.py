"""
840 Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
class Solution:
    # brutal force solution from https://blog.csdn.net/fuxuemingzhu/article/details/80473253
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        counter = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                sub_matrix = [[grid[row + i][col + j] for j in range(3)] for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter += 1
        return counter

    def magic_square(self, matrix):
        is_number_right = all(1 <= matrix[i][j] <= 9 for i in range(3) for j in range(3))
        is_row_right = all(sum(row) == 15 for row in matrix)
        is_col_right = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0] == 10
        return is_number_right and is_row_right and is_col_right and is_diagonal_right
