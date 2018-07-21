class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        思想: 使用双指针来表示一个子串. 若出现重复,就收紧左边指针.
        不重复,就继续往后扫.
        使用hash来记录最近出现字符的位置
        复杂度: 只扫了一遍,o(n)
        """
        max_lenght = 0
        buf = {}
        left = 0
        for i, c1 in enumerate(s):
            if c1 in buf:
                left = max(buf[c1] + 1, left)
            buf[c1] = i
            max_lenght = max(i - left + 1, max_lenght)
        return max_lenght


if __name__ == '__main__':
    my_s = "abba"
    s = Solution()
    print(s.lengthOfLongestSubstring(my_s))
