from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 由于要求列出全部组合,所以用回溯写一下
        candidates.sort()
        result = []
        temp = []

        def helper(index, rest):
            if rest == 0:
                result.append(temp.copy())
            elif rest < 0:
                return

            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                helper(i, rest - candidates[i])
                temp.pop()

        helper(0, target)
        return result


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solver = Solution()
    rnt = solver.combinationSum(candidates, target)
    print(rnt)
