class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_lenght = 0
        buf = {}
        left = 0
        for i, c1 in enumerate(s):
            if c1 in buf:
                left = max(buf[c1]+1,left)
            buf[c1] = i
            max_lenght = max(i - left + 1, max_lenght)
        return max_lenght


if __name__ == '__main__':
    my_s = "abba"
    s = Solution()
    print(s.lengthOfLongestSubstring(my_s))
