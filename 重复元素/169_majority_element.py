from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        num = 0
        count = 0
        for item in nums:
            if not count:
                num = item
                count = 1
            elif num == item:
                count += 1
            else:
                count -= 1
        return num


if __name__ == '__main__':
    # nums = [3, 2, 3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    solver = Solution()
    print(solver.majorityElement(nums))
