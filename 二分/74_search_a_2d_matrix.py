class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        #思入: 二本. 将一维mid 转为二维即可
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1
        while L <= R:
            mid = (L + R) // 2
            col, row = mid % n, mid // n
            temp = matrix[row][col]
            if temp == target:
                return True
            elif temp < target:
                L = mid + 1
            else:
                R = mid - 1
        return False


if __name__ == '__main__':
    nums = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    s = Solution()
    print(s.searchMatrix(nums, target))
