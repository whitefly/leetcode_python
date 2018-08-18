class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        思入: 由于此时matrix不能简单当做一维有序数组. 二分的核心是循环不变式,即结果一定剩下的部分里.按什么顺序来切出这个部分
        难点: 若对nums[0][0]来比较,右不一定<=下. 所以需要找到一个方向 a部分<b部分
        需要a部分<b部分, 只有上部分<右部分. 所以用 左下的点作为起始点
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        p_x, p_y = m - 1, 0
        while p_x >= 0 and p_y <= n - 1:
            temp = matrix[p_x][p_y]
            if temp == target:
                return True
            elif temp < target:
                p_y += 1
            else:
                p_x -= 1
        return False


if __name__ == '__main__':
    nums = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    num = 20
    s = Solution()
    print(s.searchMatrix(nums, num))
