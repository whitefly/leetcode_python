class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        content_stack = [""]
        position = -1
        size = len(s) - 1
        while position < size:
            position += 1
            c = s[position]
            if c.isdigit():
                # 处理多位数
                end = s.index("[", position)
                num_stack.append(int(s[position:end]))
                position = end - 1
            elif c == "[":
                content_stack.append("")
            elif c == "]":
                top = content_stack.pop() * num_stack.pop()
                content_stack[-1] += top
            else:
                content_stack[-1] += c
        return content_stack[-1]


if __name__ == '__main__':
    demo = "10[leetcode]"
    s = Solution()
    rnt = s.decodeString(demo)
    print(rnt)
