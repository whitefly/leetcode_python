class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        思入: x轴上2条重合直线长度 * y轴上2条重合的直接长度
        """
        s1 = self._getS(A, B, C, D)
        s2 = self._getS(E, F, G, H)
        y_width = self._intersection(B, D, F, H)
        x_width = self._intersection(A, C, E, G)

        return s1 + s2 - y_width * x_width

    @staticmethod
    def _intersection(a1, a2, b1, b2):
        left = max(a1, b1)
        right = min(a2, b2)
        return right - left if left < right else 0

    @staticmethod
    def _getS(a, b, c, d):
        return (d - b) * (c - a)


if __name__ == '__main__':
    s = Solution()
    print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
