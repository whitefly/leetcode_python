class Solution:
    map1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        思入: 每次多加一个字母,就需要添加for. 所以for的层数不知道,故必然使用递归.
        类似题目: 展平多维数组
        递推公式:f(str)会返回['as','ac'] 加这个基础上加工,然后返回.
        终止条件:最后剩下一个字母时终止递归
        """
        # result=[]
        # for chars in self.letterCombinations(digits[1:]):  #这个2重for+append完成可以使用 列表推导式简化成一行
        #     for c in self.map1[digits[0]]:
        #         result.append(c + chars)
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.map1[digits[0]])
        return [c + chars for chars in self.letterCombinations(digits[1:]) for c in self.map1[digits[0]]]


if __name__ == '__main__':
    my_str = '234'
    s = Solution()
    # print(s.letterCombinations(my_str))
