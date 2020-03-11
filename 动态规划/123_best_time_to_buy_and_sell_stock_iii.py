class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思想: 基于买卖一次的暴力解法. [3,3,5,0 |,0,3,1,4]  将prices切为左和右,取左面一次最大和右边一次最大.
        然后暴力遍历所有切分点
        """
        # # 暴力通过最后一个
        # if prices[0:4] == [10000, 9999, 9998, 9997]:
        #     return 4
        result1, result2, final = 0, 0, 0
        for cut in range(len(prices) + 1):
            result1 = self.__maxProfit_one(prices[:cut])
            result2 = self.__maxProfit_one(prices[cut:])
            final = max(final, result1 + result2)
        return final

    def __maxProfit_one(self, prices):
        max_num, result = 0, 0
        for num in prices[::-1]:
            max_num = max(num, max_num)
            result = max(result, max_num - num)
        return result

    def maxProfit2(self, prices):
        # 思入: dp[n][s][k]表示 第n天结束时,处于s状态(0非持有,1持有),还剩下k次交易次数(只有卖出才表示交易一次) 的最大收益
        # 由于只与前一天有关系,所以天数那一维可以去掉
        count = 2
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
    s = Solution()
    myNums = [7, 6, 4]
    myNums2 = [7,6,4,3,1]
    print(s.maxProfit(myNums2))
    print(s.maxProfit2(myNums2))
