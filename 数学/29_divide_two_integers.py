class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        思入: 由于不能使用除法,所以只能使用减法.
        暴力法: 每次loop都减去一个除数 复杂度(m/n). 若被除数很大, 除数很小,会导致复杂度过高
        优化: 联想之前使用的二分求幂,可以有效减少乘法的乘次. 这里可以将被除数成倍的增加. 当到顶无法除尽时,重新初始化除数
        """
        # 判断正负
        is_neg = (divisor > 0) ^ (dividend > 0)

        result = 0
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            temp_d = divisor
            temp_count = 1
            while dividend >= temp_d:
                dividend -= temp_d
                result += temp_count

                # temp进行成倍增加
                temp_d <<= 1
                temp_count <<= 1

        result = -result if is_neg else result
        return min(max(result, -2147483648), 2147483647)


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-2147483648, 1))
