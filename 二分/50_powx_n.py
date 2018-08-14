class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        思入:2分求幂,将幂化为二级制.基数不断增加
        """

        if n < 0:
            x = (1 / x)
            n = -n
        temp = x
        result = 1
        while n >= 1:
            now = n % 2
            n = n // 2
            if now == 1:
                result *= temp
            temp = temp ** 2
        return result


if __name__ == '__main__':
    a = 2.10
    n = 3
    s = Solution()
    print(s.myPow(a, n))
