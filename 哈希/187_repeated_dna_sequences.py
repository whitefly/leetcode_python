from collections import Set
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 思入: 滑动指针+hash: 将字符串压缩为数字来加快比较.但是Python的int是不会溢出的,需要另写一个函数来自定义溢出.我懒o(╥﹏╥)o
        container = set()
        result = set()
        if len(s) < 10:
            return []
        for i in range(9, len(s)):
            target = s[i - 9:i + 1]
            if target in container:
                result.add(target)
            else:
                container.add(target)
        return list(result)


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solver = Solution()
    print(solver.findRepeatedDnaSequences(s))
