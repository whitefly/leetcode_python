class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思想:简单动态规划. 每个位置需要知道的值: 它右边最大的值.
        所以一直从右向左扫,找出每个点的右边最大值
        时间复杂度: O(n)
        """
        max_num, result = 0, 0
        for num in prices[::-1]:
            max_num = max(num, max_num)
            result = max(result, max_num - num)
        return result

    def maxProfit2(self, prices):
        # 思入: dp[n][s][k]表示 第n天结束时,处于s状态(0非持有,1持有),还剩下k次交易次数(只有卖出才表示交易一次) 的最大收益
        if not prices:
            return 0
        unhold, hold, = 0, 1
        count = 2
        days = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(days)]
        dp[0][unhold][1] = 0
        dp[0][unhold][0] = 0
        dp[0][hold][1] = -prices[0]
        dp[0][hold][0] = -100000
        for i in range(1, days):
            for k in range(count):
                dp[i][1][k] = max(dp[i - 1][1][k], dp[i - 1][0][k] - prices[i], )  # 非持有,持有->持有
                dp[i][0][k] = max(dp[i - 1][0][k],
                                  -100000 if k == 1 else dp[i - 1][1][k + 1] + prices[i])  # 非持有,持有->非持有
        return max(dp[days - 1][0][0], dp[days - 1][0][1])


if __name__ == '__main__':
    my_nums = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(my_nums))
    print(s.maxProfit2(my_nums))
