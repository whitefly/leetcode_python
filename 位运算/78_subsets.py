from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 传统思入: 使用回溯法+剪枝
        # 位运算思入:[1,2,3]的左右组合c(0,3)+c(1,3)+c(2,3)+c(3,3), 组合总数就是(3)^2 这点跟2进制的长度很相似,所以遍历二进制即可
        result = []
        for i in range(2 ** len(nums)):
            result.append(Solution.invert(i, nums))
        return result

    @staticmethod
    def invert(position: int, nums: List[int]):
        index = 1
        rnt = []
        for i in range(len(nums)):
            bit = position & index
            if bit:
                rnt.append(nums[i])
            index <<= 1
        return rnt


if __name__ == '__main__':
    solver = Solution()
    nums = [1, 2, 3]
    print(solver.subsets(nums))
