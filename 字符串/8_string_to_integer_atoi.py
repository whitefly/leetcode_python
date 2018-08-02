class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digit = '0123456789' + '+-'  # 一旦第一次检测到某个,开始进入运算
        process = False
        negative = False
        result = 0
        for i in str:
            if i not in digit:
                # 非数字
                if process:
                    break
                elif i == ' ':
                    continue
                else:
                    return 0
            else:
                # 数字的情况
                if not process:
                    # 开始进入过程,将digit中的+-符号去掉, 防止+1-的情况发生
                    digit = '0123456789'
                    process = True
                    if i == '-':
                        negative = True
                    elif i == '+':
                        negative = False
                    else:
                        result = result * 10 + ord(i) - ord('0')
                else:
                    # 已经进入过程
                    result = result * 10 + ord(i) - ord('0')
        # 输出结果
        result = -result if negative else result
        if result < -2 ** 31:
            return -2 ** (31)
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result


if __name__ == '__main__':
    a = '  0000000000012345678'
    s = Solution()
    print(s.myAtoi(a))
