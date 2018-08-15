class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        思入:反向遍历得到第一个不为空格的长度. 由于出现' '后需要根据状态分开操作,所以需要设置一个状态变量process,表示已经开始第一个字符串
        类似题目: 8_string_to_integer
        """
        process = False
        count = 0
        for i in s[::-1]:
            if process:
                if i == ' ':
                    return count
                else:
                    count += 1
            else:
                if i == ' ':
                    continue
                else:
                    count += 1
                    process = True
        return count if process else 0


if __name__ == '__main__':
    my_s = "Hello World"
    s = Solution()
    print(s.lengthOfLastWord(my_s))
