class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 变种二分.  先判断子数组是是否升序.
        若升序,取l.(最后可能只有1个元素)
        若不是升序,判断mid在哪一个区间
        """
        l, r = 0, len(nums)-1

        while l <= r:

            if nums[l] <= nums[r]:
                # 数组有序
                return nums[l]
            else:
                # 数组被旋转,对mid位置进行判断
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return -1


if __name__ == '__main__':
    my_nums = [4,5,6,7,0,1,2]
    s = Solution()
    print(s.findMin(my_nums))
