class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        思入: 动态规划 状态量:到达该点的不同路径
        设置二维dp,从左到右,从上到下开始扫
        """
        dp = [[0] * n for i in range(m)]
        for x, row in enumerate(dp):
            for y, unit in enumerate(row):
                if x == 0 and y == 0:
                    dp[x][y] = 1
                elif x == 0:
                    dp[x][y] = dp[x][y - 1]
                elif y == 0:
                    dp[x][y] = dp[x - 1][y]
                else:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    my_m, my_n = 7, 3
    s = Solution()
    print(s.uniquePaths(my_m, my_n))
