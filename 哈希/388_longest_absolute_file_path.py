class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        思入: 需要找到某个文件or文件夹的父节点. 由于是顺序排下来的,所以只需要找到该层级上的最后一个文件夹即可(所以可以只用一个数组来保存该层last文件夹的字符长度即可)
        通过/t的数量来确定父节点的下标,用一个result来记录目前最长的一个
        """
        words = input.split(sep='\n')
        dp = [0] * 1024
        result = 0
        for word in words:
            # 本目录的级别
            level = word.count('\t')
            is_file = word.count('.')
            if is_file == 0:
                if level == 0:
                    dp[level] = len(word)
                else:
                    dp[level] = dp[level - 1] + len(word) - level + 1
            else:
                result = max(dp[level - 1] + len(word) - level + (0 if level == 0 else 1), result)
        return result


if __name__ == '__main__':
    one = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    s = Solution()
    print(s.lengthLongestPath(one))
    # print(len('\n'))
