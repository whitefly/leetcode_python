class Solution:
    def check(self, x):
        return ord('0') <= ord(x) <= ord('9') or ord('a') <= ord(x) <= ord('z') or ord('A') <= ord(x) <= ord('Z')

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        思入: 使用双指针,左右扫.表示对称的位置,碰到非字符串,直接跳过
        """
        # if not s:
        #     return True
        l, r = 0, len(s) - 1
        while l <= r:
            while not self.check(s[l]) and l < r:
                l += 1
            while not self.check(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    my_str = '  '
    print(s.isPalindrome(my_str))
