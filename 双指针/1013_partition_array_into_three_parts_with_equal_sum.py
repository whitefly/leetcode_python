from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # O(n^2)复杂度,直接超时
        sum_map = [0] * len(A)
        for i, num in enumerate(A):
            sum_map[i] = (0 if not i else sum_map[i - 1]) + num

        if sum_map[-1] % 3 != 0:
            return False

        def get_sum(L, R):
            return sum_map[R] - sum_map[L] + A[L]

        for i in range(1, len(A) - 1):
            for j in range(i + 1, len(A) - 1):
                if get_sum(0, i) == get_sum(i + 1, j) == get_sum(j + 1, len(A) - 1):
                    return True
        return False

    def canThreePartsEqualSum2(self, A: List[int]) -> bool:
        # 和总是会等于sum(A)/3, 这里可以继续优化:2个指针可以在同一个while中循环
        acc = 0
        for num in A:
            acc += num
        if acc % 3 != 0:
            return False
        target = acc // 3
        position, part_sum = 0, 0
        for i, num in enumerate(A):
            part_sum += num
            if part_sum == target:
                position = i
                break
        else:
            return False
        part_sum = 0
        for num in A[len(A) - 1:position + 1:-1]:
            part_sum += num
            if part_sum == target:
                return True
        return False


if __name__ == '__main__':
    nums = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    s = Solution()
    rnt = s.canThreePartsEqualSum2(nums)
    print(rnt)
