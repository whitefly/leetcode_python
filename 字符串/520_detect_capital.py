class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 思入: 有限状态机 初始,首大,首小,全大,全小,正常,错误
        mapping = [[1, 3, 6, 3, 6, 6, 6], [2, 5, 4, 6, 4, 5, 6]]
        status = 0
        for c in word:
            status = mapping[int(c.islower())][status]
            if status == 6:
                return False
        return True



if __name__ == '__main__':
    target = "Leetcode"
    solver = Solution()
    print(solver.detectCapitalUse(target))
