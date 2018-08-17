from pprint import pprint


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        思入: 暴力扫,批量设置0.
        已经优化: 用set来分别存 要删除的列和行. 然后批量设置 最坏的空间复杂度还是为x+y.
        待优化: 不需要用set来存, 直接放在第一个为0的点的行,列来存. 这样只需要常数空间 不过会增加条件判断.不想写
        """
        target_x, target_y = set(), set()
        m, n = len(matrix), len(matrix[0])
        for x, row in enumerate(matrix):
            for y, unit in enumerate(row):
                if matrix[x][y] == 0:
                    target_x.add(x)
                    target_y.add(y)
        # 批量对横,列进行归0
        for x in target_x:
            for i in range(n):
                matrix[x][i] = 0
        for y in target_y:
            for i in range(m):
                matrix[i][y] = 0


if __name__ == '__main__':
    nums = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    s = Solution()
    s.setZeroes(nums)
    pprint(nums)
