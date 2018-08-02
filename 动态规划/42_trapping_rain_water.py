class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        思入:一个点的含水量,取决于左边最高和右边最高. min(左最高,右最高)-本身高   就是该点含水量. 所以需要计算 左最高和右最高的数组
        """
        l_highest = []
        last_highest = 0
        for i in height:
            last_highest = max(last_highest, i)
            l_highest.append(last_highest)
        # 右扫
        last_highest = 0
        result = 0
        for i, v in enumerate(reversed(height)):
            last_highest = max(last_highest, v)
            result += min(last_highest, l_highest[len(height) - 1 - i]) - v
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
