class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == x[::-1]
