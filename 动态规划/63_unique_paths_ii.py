class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        思入: 暴力dp. 碰到障碍物就跳过.默认该点dp=0
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        for x, row in enumerate(obstacleGrid):
            for y, unit in enumerate(row):
                if unit == 1:
                    continue
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
    nums = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    s = Solution()
    print(s.uniquePathsWithObstacles(nums))
