class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        #思入: 每扫一点,将该点未来可以跳跃的点都设置为True,表示可以到达. 最后查看最后一点是否为True.
        缺点: 重复变为True太高,不需要dp.只需要一个index,index之前的都是True.
        若扫到的点达不到,说明出现断层.直接返回False
        """
        last = 0
        for i, v in enumerate(nums):
            if last >= i:
                last = max(v + i, last)
                if last >= len(nums) - 1:
                    return True
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    my_nums = [3, 2, 1, 0, 4]
    print(s.canJump(my_nums))
