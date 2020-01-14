class Solution:
    def reverseBits(self, n: int) -> int:
        # 思入: 通过位运算来颠倒,32位,需要移动5次

        magic = 0x0000ffff
        n = (n & magic) << 16 | (n & ~magic) >> 16
        magic = 0x00ff00ff
        n = (n & magic) << 8 | (n & ~magic) >> 8
        magic = 0x0f0f0f0f
        n = (n & magic) << 4 | (n & ~magic) >> 4
        magic = 0x33333333
        n = (n & magic) << 2 | (n & ~magic) >> 2
        magic = 0x55555555
        n = (n & magic) << 1 | (n & ~magic) >> 1
        return n


if __name__ == '__main__':
    a = 1
    solver = Solution()
    print(solver.reverseBits(a))
