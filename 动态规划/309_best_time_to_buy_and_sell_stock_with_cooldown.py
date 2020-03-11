from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思入: 分3种状态 非持有0,持有1,冷冻期2
        dp = [-100000] * 3
        temp = dp.copy()
        dp[0] = 0
        for price in prices:
            temp[0] = max(dp[0], dp[2])
            temp[1] = max(dp[1], dp[0] - price)
            temp[2] = dp[1] + price

            temp, dp = dp, temp
        return max(dp)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    s = Solution()
    rnt = s.maxProfit(prices)
    print(rnt)
