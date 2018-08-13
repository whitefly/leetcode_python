from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        思入: 核心:怎么对每一个字符串得到一个key(每一个字母相同排序不同的字符串key相同). 排序法,直接对每个str进行排序,转为为统一的顺序作为key
        复杂度:主要对每个进行排序 O(n*mlogm), m个每个单词的长度
        """
        buf = {}
        for one in strs:
            sign = tuple(sorted(one))
            if sign in buf:
                buf[sign].append(one)
            else:
                buf[sign] = [one]
        return list(buf.values())


class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        思入: 将26的字母出现的频率tuple作为key. 这样就可以不用排序
        """
        buf = {}
        for one in strs:
            sign = tuple(sorted(one))
            if sign in buf:
                buf[sign].append(one)
            else:
                buf[sign] = [one]
        return list(buf.values())

    def get_count(self, my_str):
        pass


if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(a))
