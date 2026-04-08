class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        r = len(s)-1
        l = 0
        while r > l:
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1
        return True
