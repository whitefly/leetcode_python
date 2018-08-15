class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        思入1: 一圈又一圈,看做递归. f(n)表示圈内的数列,f(n+1表示内圈的所有数列). f(n)=本圈数列+f(n-1)
        """
        if not matrix:
            return []
        return self.hehe(matrix, (0, 0))

    def hehe(self, matrix, position):
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        x, y = position
        # 4个角点
        x_, y_ = m - x, n - y
        if x > x_ or y > y_:
            return []
        if x_ == x and y_ == y:
            temp = [matrix[x][y]]  # 一点
        elif x_ == x:
            temp = matrix[x][y:y_ + 1]  # 在一条横线上
        elif y_ == y:
            temp = [matrix[i][y] for i in range(x, x_ + 1)]  # 在一条竖线上
        else:
            temp = matrix[x][y:y_] + [matrix[i][y_] for i in range(x, x_)] + matrix[x_][y_:y:-1] + [
                matrix[i][y] for i in range(x_, x, -1)]  # 围一个圈 上+左+下+右
        return temp + self.hehe(matrix, (x + 1, y + 1))


class Solution1:
    def spiralOrder(self, matrix):
        """
        :param matrix:
        :return:
        思入:非递归写法. 使用循环来确定4个点. 将单纯的横看做上, 将单纯的竖看做 上+右
        """
        if not matrix:
            return matrix
        # 四个角点
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1
        result = []
        while row_begin <= row_end and col_begin <= col_end:
            # 上
            result.extend(matrix[row_begin][col_begin:col_end + 1])
            # 右
            if row_begin < row_end:
                result.extend([matrix[i][col_end] for i in range(row_begin + 1, row_end + 1)])
                if col_begin < col_end:
                    # 下
                    result.extend(matrix[row_end][col_end - 1:col_begin:-1])
                    # 左
                    result.extend([matrix[i][col_begin] for i in range(row_end, row_begin, -1)])
            row_begin += 1
            row_end -= 1
            col_begin += 1
            col_end -= 1
        return result


if __name__ == '__main__':
    a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    s = Solution1()
    print(s.spiralOrder(a))
