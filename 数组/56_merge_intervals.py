# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: list[Interval]):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        思入: 由于区间可能不是从左到右排序的,导致不到处理.所以先从左到右排下序
        """
        if not intervals:
            return []
        intervals.sort(key=lambda s: s.start)
        result = [intervals[0]]
        for i in intervals:
            last = result[-1]
            if last.start <= i.start <= last.end:
                # 合并
                last.end = max(last.end, i.end)
            else:
                # 新增
                result.append(i)
        return result
