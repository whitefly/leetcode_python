import math
import sys


class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        num = num if x >= 0 else -num
        return num if -0x7fffffff <= num < 0x7fffffff else 0


if __name__ == '__main__':
    target = -0xffffffff
    solver = Solution()
    result = solver.reverse(target)
    print(result)
