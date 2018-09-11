class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        正则分割,map函数逐个翻转
        """
        import re
        pat = re.compile(r'\s+')
        strs = [i for i in pat.split(s) if i][::-1]
        return ' '.join(strs)


class Solution(object):
    def reverseWords(self, s):
        """
        :param s:str
        :return:
        思想: str.split()会自动区分读个空格.所以不需要使用正则
        """
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    my_strs = "   111   2222   "
    # s = Solution()
    # print(s.reverseWords(my_strs))
    print(my_strs.split())
