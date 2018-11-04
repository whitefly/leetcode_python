class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        思入:第一个想法就是动态规划,但是问题是需要知道4个方向比较后才知道该点的最优解. 按遍历顺序下,只能先知道上和右
        解决方法:遍历2遍,第一次为左上,第二次为下,右
        """
        big_num = 99999999
        m, n = len(matrix), len(matrix[0])
        dp = [[big_num] * n for i in range(m)]

        # 左上最优遍历
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    up = dp[i - 1][j] if i - 1 >= 0 else big_num
                    left = dp[i][j - 1] if j - 1 >= 0 else big_num
                    dp[i][j] = min(up + 1, left + 1)
        # 右下最优遍历
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp[i][j] == 0:
                    continue
                down = dp[i + 1][j] if i + 1 <= m - 1 else big_num
                right = dp[i][j + 1] if j + 1 <= n - 1 else big_num
                dp[i][j] = min(down + 1, right + 1, dp[i][j])
        return dp


if __name__ == '__main__':
    s = Solution()
    my_M = [[0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1]]
    print(s.updateMatrix(my_M))
