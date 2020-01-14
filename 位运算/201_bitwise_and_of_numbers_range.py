class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 思入:  同一位中,1都是周期性连续出现,一旦给出的范围超过这个周期,那么此时按位与后,一定是0.
        # 所以只需要算出每一位的周期即可,只要范围是否在周期中,初始化+余数
        # 0位的周期是1, 1位的周期是2,2位的周期是4
        T = 1  # 周期
        result = 0
        for i in range(32):
            num_id = m // T  # 经历的周期数  3/2=1 余数是1
            num_rest = T - m % T
            if num_id % 2 == 1 and (n - m + 1) <= num_rest:
                result += (1 << i)
            T <<= 1
        return result

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        # 思入: 只需要m和n的功能前缀,若没有公共前缀,那么就是0
        # why???
        #
        pass


if __name__ == '__main__':
    m = 0
    n = 1
    solver = Solution()
    print(solver.rangeBitwiseAnd(m, n))
