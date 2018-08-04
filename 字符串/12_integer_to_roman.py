class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        思入:本质就是一个进制转化
        """
        m = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'),
             (4, 'IV'), (1, 'I'))
        result = ''
        for v, c in m:
            if num // v != 0:
                result += c * (num // v)
                num %= v
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(4))
