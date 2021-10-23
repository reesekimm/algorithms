# https://leetcode.com/problems/valid-palindrome/

# 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(''.join(filter(str.isalnum, s)).lower())
        
        if len(l) is 1:
            return True
        
        for i in range(len(l)):
            end = i + 1
            if l[i] != l[-end]:
                return False
        
        return True


# 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = [i for i in s.lower() if i.isalnum()]
        return alnum == alnum[::-1]
