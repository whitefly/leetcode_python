class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        思入1:取第一个,每次第n的字符串和所有strs的第n的字符进行比较.,慢慢增加字符.一旦不符合,就返回
        """
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]
        result = ''
        for i, c in enumerate(strs[0]):
            for other in strs[1:]:  # 优化点:直接使用strs,就可以不用判断是否存在越界的问题
                if not (i < len(other) and other[i] == c):
                    return result
            else:
                result += c
        return result


class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :param strs:
        :return:
        思如2: 思入1的优化,(使用最短的那个最为初始化前缀).其他和思如1一样. 使用切边来得到 要返回的前缀子串
        """
        if not strs:
            return ''
        result = min(strs, key=len)
        for i, c in enumerate(result):
            for other in strs:
                if other[i] != c:
                    return result[:i]
        return result


class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :param strs:
        :return:
        思如3:每次选出2个字符串的公共前缀.然后拿这个公共前缀和第3个字符串去比较, 类似reduce的思想.
        """
        if not strs:
            return ''
        result = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            while not s.startswith(result):
                result = result[:-1]
        return result


if __name__ == '__main__':
    s = Solution1()
    my_strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(my_strs))
