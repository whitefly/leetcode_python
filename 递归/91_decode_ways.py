class Solution:

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        思入:从左向右遍历,一个字母可能有1或者2个数字表示. 若第一个为1个数字编码,递归剩下的[1:]. 若取2个数字进行编码,递归剩下的[2:]. 返回2个相加的结果
        """
        buf = [-1] * len(s)

        def hehe(s):
            if buf[len(s) - 1] != -1:
                return buf[len(s) - 1]

            if s[0] != '0':
                if len(s) == 1:
                    return 1
                count1 = hehe(s[1:])
            else:
                return 0

            if 10 <= int(s[:2]) <= 26:
                if len(s) == 2:
                    return 1 + count1
                count2 = hehe(s[2:])
            else:
                return count1

            buf[len(s) - 1] = count2 + count1
            return count2 + count1

        return hehe(s)


class Solution1:
    def numDecodings(self, s):
        """
        :param s:
        :return:
        思入:动态规划dp写法,   dp为含有右边全部字符的 编码方式.
        状态转移方程 dp[i]=dp[i+1]+dp[i+2]    当本身作为1个编码或者2个编码都不存在时,不能直接dp[i+11] 或者 dp[i+2]
        """
        dp = [0] * len(s) + [1]
        size = len(s)
        for i in range(len(s) - 1, -1, -1):
            count1 = dp[i + 1] if s[i] != '0' else 0
            count2 = dp[i + 2] if (i < size - 1 and 10 <= int(s[i:i + 2]) <= 26) else 0
            dp[i] = count1 + count2
        return dp[0]


if __name__ == '__main__':
    s = Solution1()
    print(s.numDecodings(
        "100"))
