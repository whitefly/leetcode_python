class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        #思入: 回溯剪枝-即深度优先.  准备一个temp来存储节点, 准备一个result来收集满足的temp.  设定终止条件(深度), 和递归下一层的方式
        """
        result, temp = [], []
        size = len(s)

        def helper(index):
            # 终止条件
            if len(temp) < 4 and index == size:
                return
            if len(temp) == 4 and index < size:
                return
            if len(temp) == 4 and index == size:
                result.append('.'.join(temp))
                return

            for i in range(1, 4):
                a = int(s[index:index + i])

                if i == 2 and not (10 <= a <= 99):
                    continue
                if i == 3 and not (100 <= a <= 255):
                    continue
                temp.append(s[index:index + i])
                helper(index + i)
                temp.pop()

        helper(0)
        return result


if __name__ == '__main__':
    demo = "662497987"
    s = Solution()
    hehe = s.restoreIpAddresses(demo)
    print(hehe)
