class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        思想: 子串-->2维dp. 推导式:  小范围成立-->大范围才可能成立
        """
        dp = [[0 for i in range(len(s))] for i in range(len(s))]
        max_count, result = 0, ''
        for i, right in enumerate(s):
            for j, left in enumerate(s[:i + 1]):
                dp[j][i] = (left == right) and (dp[j + 1][i - 1] if (i - j) > 2 else True)
                if dp[j][i] and i - j >= max_count:
                    max_count = i - j + 1
                    result = s[j:i + 1]
        return result


if __name__ == '__main__':
    my_str = "abcda"
    s = Solution()
    print(s.longestPalindrome(my_str))
