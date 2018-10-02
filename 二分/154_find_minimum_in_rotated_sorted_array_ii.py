class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 类似于搜索旋转数据ii. 首先对旋转组数的2边进行去重(严格变为大小,二边).
        """
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while nums[l] == nums[r] and l < r:
            # 去掉重复
            r -= 1
        while l <= r:
            if nums[l] <= nums[r]:
                # 数组有序
                return nums[l]
            else:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    # 在高的位置
                    l = mid + 1
                else:
                    # 在低的位置
                    r = mid
        return nums[l]


if __name__ == '__main__':
    my_nums = [2, 2, 2, 0, 1]
    s = Solution()
    print(s.findMin(my_nums))
