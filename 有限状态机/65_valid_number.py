"""
思入:
方法1: 高级版->比较多条件,利用有限状态机
方法2: 初级版->写个re正则
方法3: 无脑版->利用python的float()


状态机中实现中的一些坑
1.'-.1','3.e3'可以过
2.'.'过不了

"""


class Solution:
    Digit = 0
    Signal = 1
    Blank = 2
    Dot = 3
    E = 4
    Other = 5
    End = 6

    T = 98
    F = 99

    statusTable = [
        [2, 1, 0, 9, F, F, F],  # 开始态0
        [2, F, F, 9, F, F, F],  # 符号态1
        [2, F, 8, 3, 5, F, T],  # 数字态(整数部分,非e)
        [4, F, 8, F, 5, F, T],  # 小数点态(有整数部分  例子'1.', 分开小数点状态是为了防止'.'通过)
        [4, F, 8, F, 5, F, T],  # 数字态(小数部分,非e)
        [7, 6, F, F, F, F, F],  # e态
        [7, F, F, F, F, F, F],  # 符号态(e幂符号)
        [7, F, 8, F, F, F, T],  # 数字态(e幂数值)
        [F, F, 8, F, F, F, T],  # 空格态
        [4, F, F, F, F, F, F]  # 小数点态(无整数部分,例'.1')
    ]

    def get_element(self, c):
        if 48 <= ord(c) <= 57:
            return self.Digit
        if c == ' ':
            return self.Blank
        if c == "+" or c == '-':
            return self.Signal
        if c == '\0':
            return self.End
        if c == 'e':
            return self.E
        if c == '.':
            return self.Dot
        else:
            return self.Other

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = s + '\0'  # 手动加一个\0结束符,在静态语言中是不用加的
        now_S = 0
        for c in string:
            e = self.get_element(c)
            now_S = (self.statusTable[now_S])[e]  # 输入行为后,新转移后的状态
            if now_S == self.T or now_S == self.F:
                return now_S == self.T

    def isNumber2(self, s):
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    a = "35.e3 1"  # '-.1'
    s1 = Solution()
    print(s1.isNumber2(a))
