class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        思入: 本次字符串的处理需要用到上一次的,很自然地使用递归.将f(n-1)看做一个已知字符串即可.
        本题字符串容量不少,在n=50时,已经达到90w的字符串. 最后应该越来越多(伪几何增长).使用
        """
        if n == 1:
            return "1"
        else:
            content = self.countAndSay(n - 1)
            temp = content[0]
            count, result = 0, ''
            for index, i in enumerate(content):
                if i != temp:
                    result += "{}{}".format(count, temp)
                    temp, count = i, 1
                else:
                    count += 1
                # 处理末尾情况
                if index == len(content) - 1:
                    result += "{}{}".format(count, temp)
            return result


if __name__ == '__main__':
    s = Solution()
    a = len(s.countAndSay(50))
    print(a)
