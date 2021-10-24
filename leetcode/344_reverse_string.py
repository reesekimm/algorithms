# https://leetcode.com/problems/reverse-string/

# 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = 0
        while count < len(s) - 1:
            s.insert(count, s.pop())
            count += 1

# 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        