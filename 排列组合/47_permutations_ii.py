from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []
        gone = [False] * len(nums)

        def helper():
            if len(temp) == len(nums):
                result.append(temp.copy())
                return

            for i in range(len(nums)):
                if gone[i]:
                    continue
                if i > 0 and not gone[i - 1] and nums[i - 1] == nums[i]:
                    continue
                temp.append(nums[i])
                gone[i] = True
                helper()
                temp.pop()
                gone[i] = False

        helper()
        return result


if __name__ == '__main__':
    nums = [1]
    solver = Solution()
    print(solver.permuteUnique(nums))
