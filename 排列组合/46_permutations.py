from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []
        gone = [False] * len(nums)

        def helper():
            if len(temp) == len(nums):
                result.append(temp.copy())
                return

            for i in range(len(nums)):
                if not gone[i]:
                    temp.append(nums[i])
                    gone[i] = True
                    helper()
                    temp.pop()
                    gone[i] = False

        helper()
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    solver = Solution()
    print(solver.permute(nums))
