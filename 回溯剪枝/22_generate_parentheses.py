from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # 思入: 构造一个数, 记录还剩下多少(没有用完, 子树为 ( 和  ),记录同一个路径上( 和 ) 的个数
        self.container = []
        self.result = []
        self.helper(0, 0, n)
        return self.result

    def helper(self, l_count, r_count, n):
        if l_count == r_count == n:
            self.result.append("".join(self.container))
            return
        elif l_count > n or r_count > n or l_count < r_count:
            return

        for item in ["(", ")"]:
            if item == "(":
                l_count += 1
                self.container.append(item)
                self.helper(l_count, r_count, n)
                self.container.pop()
                l_count -= 1
            else:
                r_count += 1
                self.container.append(item)
                self.helper(l_count, r_count, n)
                self.container.pop()
                r_count -= 1


if __name__ == '__main__':
    solver = Solution()
    result = solver.generateParenthesis(1)
    print(result)
