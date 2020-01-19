from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        temp = []

        def helper(index, rest):
            if rest == 0:
                result.append(temp.copy())
            elif rest < 0:
                return

            for i in range(index, len(candidates)):
                if i != index and candidates[i - 1] == candidates[i]:
                    continue
                temp.append(candidates[i])
                helper(i + 1, rest - candidates[i])
                temp.pop()

        helper(0, target)
        return result


if __name__ == '__main__':
    candidates = [2, 5, 2, 1, 2]
    target = 5
    solver = Solution()
    rnt = solver.combinationSum2(candidates, target)
    print(rnt)
