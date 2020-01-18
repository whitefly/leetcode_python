"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    num_map = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def romanToInt(self, s: str) -> int:
        index = 0
        size = len(s)
        result = 0
        while index < size:
            for item in Solution.num_map:
                if s.startswith(item, index):
                    result += Solution.num_map[item]
                    index += len(item)
        return result


if __name__ == '__main__':
    target = "IX"
    expect = 9
    solver = Solution()
    rnt = solver.romanToInt(target)
    assert rnt == expect
