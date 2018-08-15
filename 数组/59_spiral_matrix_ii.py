from pprint import pprint


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        思入: 先生成矩阵,然后按顺序填入顺序
        """
        matrix = [[1] * n for i in range(n)]
        # 四个角点
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1
        id = 1
        while row_begin < row_end and col_begin < col_end:
            # 上
            for i in range(col_begin, col_end):
                matrix[row_begin][i] = id
                id += 1
            # 右
            for i in range(row_begin, row_end):
                matrix[i][col_end] = id
                id += 1
            # 下
            for i in range(col_end, col_begin, -1):
                matrix[row_end][i] = id
                id += 1
            # 左
            for i in range(row_end, row_begin, -1):
                matrix[i][col_begin] = id
                id += 1
            row_begin += 1
            row_end -= 1
            col_begin += 1
            col_end -= 1
        if row_begin == row_end:
            matrix[row_begin][row_end] = id
        return matrix


if __name__ == '__main__':
    n = 2
    s = Solution()
    pprint(s.generateMatrix(n))
