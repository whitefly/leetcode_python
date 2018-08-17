class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        思入: 将目录名提出来,形成一个stack. 类似计算操作符,不断出栈或者忽略,最后的结果在合并即可
        """
        names = path.split('/')
        result = []
        for i in names:
            if i == '..':
                if result:
                    result.pop()
            elif i == '.' or i == '':
                continue
            else:
                result.append(i)
        return '/' + '/'.join(result)


if __name__ == '__main__':
    demo = '/..'
    s = Solution()
    print(s.simplifyPath(demo))
