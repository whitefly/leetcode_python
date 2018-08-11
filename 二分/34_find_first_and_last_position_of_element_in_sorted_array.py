class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        思入1: 一次二分+附近查找  或者 使用2次二分
        """

        l, r = 0, len(nums) - 1
        # 找第一次出现的数
        first, last = -1, -1
        if not nums:
            return first, last

        # 最后会剩下1个
        while r - l + 1 > 1:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[r] == target:
            first = r

        # 找第二次出现的,在first附近找
        if first == -1:
            return first, last
        else:
            for i, v in enumerate(nums[first:]):
                if v != target:
                    break
                else:
                    last = i + first

        return first, last


if __name__ == '__main__':
    my_nums = [2, 2]
    s = Solution()
    print(s.searchRange(my_nums, 2))
