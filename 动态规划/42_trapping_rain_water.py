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


class Solution1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        思入:本质思想没有改变,min(左最高,右最高)-本身高.
        但可以用双指针优化.只需要缩小双时针范围,o(2n) 优化为 o(n)
        对于左指针的点来说,左局部最高一定为左最高; 右指针点来说,右局部最高一定为右最高
        若左最高<右边临时最高.且因为右边临时最高<右最高.所以此时min(左最高,右最高)=左最高.不需要计算出右最高.就可以直接得出左指针点的含水量
        """
        l, r = 0, len(height) - 1
        l_high, r_high = 0, 0
        result = 0
        while l <= r:
            l_high = max(height[l], l_high)
            r_high = max(height[r], r_high)
            if l_high <= r_high:
                result += l_high - height[l]
                l += 1
            else:
                result += r_high - height[r]
                r -= 1
        return result


if __name__ == '__main__':
    s = Solution1()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
