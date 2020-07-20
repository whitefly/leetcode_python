class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        rest = list(range(1, n + 1))  # [1,2,3...n]
        # 计算1!....n!
        fac = [1]
        for i in range(1, n):
            fac.append(fac[-1] * i)
        # 根据当前k确定当前首位
        result = ""
        for i in range(n - 1, -1, -1):
            first = k // fac[i]
            k %= fac[i]
            result += str(rest.pop(first))  # 从rest中剔除
        return result


if __name__ == '__main__':
    s = Solution()
    rnt = s.getPermutation(4, 9)
    print(rnt)
