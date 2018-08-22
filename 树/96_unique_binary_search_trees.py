class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        思入: 动态规划.左子的可能*右子的可能   f(n)= f(0)*f(n-1)+f(1)*f(n-2)+f(2)*f(n-3)+...+f(n-1)*f(0)
        待优化: 这个递推式是对称的,怎么只计算一半即可?
        """
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            for z in range(0, i):
                dp[i] += dp[z] * dp[i - z - 1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(10))
