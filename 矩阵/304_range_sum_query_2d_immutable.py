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
        self.buf = [[0] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.get_sum(i, j)

    def get_sum(self, row, col):
        # 只需要在(col-1,row)的基础上,加上 (col,0~row)即可

        right = self.buf[row][col - 1] if col - 1 >= 0 else 0
        up = self.buf[row - 1][col] if row - 1 >= 0 else 0
        front = self.buf[row - 1][col - 1] if (row - 1 >= 0 and col - 1 >= 0) else 0

        self.buf[row][col] = right + up - front + self.M[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        思入:类似于之前写的数组环,用特定的值来组合成要求的值
        """
        if self.n == 0:
            return None
        s1 = self.buf[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        s2 = self.buf[row2][col1 - 1] if col1 - 1 >= 0 else 0
        s3 = self.buf[row1 - 1][col2] if row1 - 1 >= 0 else 0
        s4 = self.buf[row2][col2]

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
