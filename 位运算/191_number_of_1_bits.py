class Solution:
    def hammingWeight(self, n: int) -> int:
        # 思入: 位运算操作, n&(n-1) 去掉左边的1
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count


if __name__ == '__main__':
    num = 4
    solver = Solution()
    print(solver.hammingWeight(num))
