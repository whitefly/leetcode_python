class Solution:
    def hIndex(self, citations: list):
        """
        :type citations: List[int]
        :rtype: int
        思想1: 排序,设置一个cut,切为左和右, 右边都>= cut的值  左边都<=cut的值
        """
        # if not citations:
        #     return 0
        citations.sort()
        for cut in range(len(citations), -1, -1):
            h = len(citations) - cut
            r = all([i >= h for i in citations[cut:]])
            l = all([i <= h for i in citations[:cut]])
            if r and l:
                return h


if __name__ == '__main__':
    my_nums = []
    s = Solution()
    print(s.hIndex(my_nums))
