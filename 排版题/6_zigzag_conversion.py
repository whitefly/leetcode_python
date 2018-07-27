class Solution:
    def get_index(self, s, numRows, id):
        """
        计算每一行的的下标,然后拼接成字符串.K
        """
        gap = (numRows - 1) * 2
        result = []
        for k in [i for i in range(id, len(s), gap)]:
            if id <= k < len(s):
                result.append(k)
            if len(s) > k + (2 * numRows - id * 2 - 2) and id != (numRows - 1) and id != 0:
                result.append(k + (2 * numRows - id * 2 - 2))
        return result

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        my_str = ''
        for i in range(numRows):
            row = ''.join([s[index] for index in self.get_index(s, numRows, i)])
            my_str += row
        return my_str


if __name__ == '__main__':
    s = Solution()
    print(s.convert('ABCD', 3))
