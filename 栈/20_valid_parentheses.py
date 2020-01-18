class Solution:
    word_map = {
        "(": None,
        ")": "(",
        "{": None,
        "}": "{",
        "[": None,
        "]": "["
    }

    def isValid(self, s: str) -> bool:
        if len(s) & 1 == 1:
            return False
        stack = []
        for c in s:
            need = Solution.word_map[c]
            if need:
                if stack and stack[-1] == need:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


if __name__ == '__main__':
    target = "{[]}"
    solver = Solution()
    result = solver.isValid(target)
    print(result)
