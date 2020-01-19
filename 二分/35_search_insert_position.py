from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    num = 2
    print(bisect.bisect_left(nums, num))
