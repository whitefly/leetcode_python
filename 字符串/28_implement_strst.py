class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


class Solution1:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


class Solution2:
    def force_find(boss: str, substr: str):
        """思想:当一轮失败时,up的指针向左移动一位,然后开始新一轮的匹配
        复杂度: O(m*n)
        待优化: 使用kmp优化
        """
        up_l, up_r, down = 0, 0, 0
        while up_r < len(boss) and down < len(substr):
            # 因为新一轮时,up_r总是等于up_l
            if boss[up_r] == substr[down]:
                up_r += 1
                down += 1

            else:
                down = 0
                up_l += 1
                up_r = up_l
        # 循环退出后只有2种结果
        if down == len(substr):
            return up_l
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    total = 'aaaaa'
    sub = 'bba'
    # print(s.strStr(total, sub))
