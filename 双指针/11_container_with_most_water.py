class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        思入: 由于是容器,左右2边,想到使用双指针. 然后进行怎么移动才能得到最大值? 较短的边进行移动缩小范围,慢慢减少范围(保持宽度不变,改变高度).
        """
        l, r = 0, len(height) - 1
        result = 0
        while r - l + 1 >= 1:
            result = max(result, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
                while height[l - 1] >= height[l] and l < r:  # 优化一下,无效比较直接快进
                    l += 1
            else:
                r -= 1
                while height[r] <= height[r + 1] and l < r:
                    r -= 1
        return result


if __name__ == '__main__':
    my_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(my_list))
