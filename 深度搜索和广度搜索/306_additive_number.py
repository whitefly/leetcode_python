class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        思入:字符串拆分,然后判断是否符合某种规律
        helper返回true or false
        """

        def helper(num1: str, num2: str, rest: str):
            if rest == "":
                return False

            num3 = int(num1) + int(num2)
            first_str = str(num3)
            if rest.startswith(first_str):
                return True if len(first_str) == len(rest) else helper(num2, first_str, rest[len(first_str):])
            else:
                return False

        # 寻找开头2个数的组合
        for index1 in range(len(num)):
            for index2 in range(index1 + 1, len(num)):
                one, two = num[:index1 + 1], num[index1 + 1:index2 + 1]
                if (not one.startswith('0') or one == "0") and (not two.startswith('0') or two == "0"):
                    if helper(one, two, rest=num[index2 + 1:]):
                        return True
        return False


if __name__ == '__main__':
    my_num = "101"
    s = Solution()
    print(s.isAdditiveNumber(my_num))
