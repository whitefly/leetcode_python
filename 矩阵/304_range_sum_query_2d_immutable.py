from functools import reduce
from operator import add


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.M = matrix
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m else 0
        self.dp = [[0] * (self.n + 1) for i in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + self.M[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        思入:类似于之前写的数组环,用特定的值来组合成要求的值.
        dp[i][j]表示(0,0)~(i,j)和. 然后组合公式为: 结果=s4 - (s2 + s3 - s1)
        trick: 为了避免越界,在多加一列和一行在最后.防止dp[0][-1]报错
        """
        if self.n == 0:
            return None
        s1 = self.dp[row1 - 1][col1 - 1]
        s2 = self.dp[row2][col1 - 1]
        s3 = self.dp[row1 - 1][col2]
        s4 = self.dp[row2][col2]

        return s4 - (s2 + s3 - s1)


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    my = NumMatrix(matrix)
    print(my.sumRegion(1, 2, 2, 4))
