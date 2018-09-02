class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        思想: 2种想法: 1.使用深度优先来递归分割.   2.动态规划:搞出一个不好想的dp状态量
        主要问题是 catsandog~["cats", "dog", "sand", "and", "cat"],每个单词都有,但就是无法组成
        dp解法:
        状态量dp[i] 表示 字符串s[:i]能否拆分成符合要求的子字符串.
        状态转为为 若 str[j+1:i+1]在字符串中,且dp[j]为True(表示str[:j]可以被成功分割).那么dp[i]为True. 否则为False
        """

        dp = [False] * len(s) + [True]
        for i in range(len(s)):
            for j in range(-1, i):
                if dp[j] and (s[j + 1:i + 1] in wordDict):
                    dp[i] = True
                    break
        return dp[-2]


if __name__ == '__main__':
    s = Solution()
    my_hehe = 'applepenapple'
    my_dict = ["apple", "pen"]
    print(s.wordBreak(my_hehe, my_dict))
