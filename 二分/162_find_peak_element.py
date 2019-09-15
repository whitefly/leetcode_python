from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid
        return r if nums[l] < nums[r] else l


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    s = Solution()
    print(s.findPeakElement(nums))
