from pprint import pprint


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        思入1: 回溯算法. 给定一个index. 表示index之前的都可以被搞定. 返回0~index的所有组合
        回溯是不断向前即f(n)->f(n+1)(规定上界), 有递推式的递推是求f(n),先求f(n-1): 规定下界
        help返回所有s的所有组合str
        """
        buff = {}

        def helper(s: str):
            if not s:
                return ['']
            if s in buff:
                return buff[s]

            temp = []
            for word in wordDict:
                if s.startswith(word):
                    all = helper(s[len(word):])
                    temp += [word + (' ' if i else '') + i for i in all]
            buff[s] = temp
            return temp

        return helper(s)


if __name__ == '__main__':
    my_str = "aaaaaaaaaaaaaaa"
    my_dict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    s = Solution()
    pprint(s.wordBreak(my_str, my_dict))
