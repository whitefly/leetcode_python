from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2:
            # 动态规划法 dp[n][s]表示 第n天结束时,处于s状态(0非持有,1持有)的最大收益
            unhold, hold = 0, -100000
            for price in prices:
                new_hold = max(hold, unhold - price)
                new_unhold = max(unhold, hold + price)
                hold, unhold = new_hold, new_unhold
            return unhold
        else:
            count = k
            dp = [[0] * (count + 1) for _ in range(2)]
            temp = dp.copy()
            dp[1] = [-100000] * (count + 1)
            for price in prices:
                for k in range(count + 1):
                    temp[0][k] = max(dp[0][k], -100000 if k == count else dp[1][k + 1] + price)
                    temp[1][k] = max(dp[1][k], dp[0][k] - price)
                temp, dp = dp, temp
            return max(dp[0])


if __name__ == '__main__':
    nums = [3, 2, 6, 5, 0, 3]
    k = 2
    s = Solution()
    rnt = s.maxProfit(k, nums)
    print(rnt)
