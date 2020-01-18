import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))


if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    solver = Solution()
    result = solver.isMatch(s, p)
    print(result)
