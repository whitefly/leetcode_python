class Solution:

    def get_Near(self, a):
        return [a[:i] + chr(id) + a[i + 1:] for id in range(ord('a'), ord('z') + 1) for i in range(len(a))]

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        思入: 由于是最短,深度遍历不行,采用广度遍历.临近的字符串作为子元素. 由于在层数,所以用一个begin来每层开始的位置
        待优化: 复杂度太高,第30个测试例子总是超时. 关键在于 找相近元素太耗时. 层次遍历的逻辑可以简化下.用空间换时间

        """
        from collections import deque
        buf = set(wordList)
        if endWord not in buf:
            return 0
        q = deque()
        q.append(beginWord)
        deep = 0
        first = beginWord
        exist_f = True
        while len(q):
            temp = q.pop()
            if temp == first:
                deep += 1
                exist_f = False
            for v in self.get_Near(temp):
                if v in buf:
                    if not exist_f:
                        first = v
                        exist_f = True
                    q.appendleft(v)
                    buf.remove(v)
                    if v == endWord:
                        return deep + 1
        return 0


if __name__ == '__main__':
    my_beginWord = "hit"
    my_endWord = "cog"
    my_wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    s = Solution()
    print(s.ladderLength(my_beginWord, my_endWord, my_wordList))
