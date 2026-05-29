class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalpha() and not s[i].isdigit() and i < j:
                i += 1
            while not s[j].isalpha() and not s[j].isdigit() and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True