class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        first = 0
        last = 0
        char = set()
        while last < len(s):
            if s[last] not in char:
                char.add(s[last])
                last += 1
            else:
                char.remove(s[first])
                first += 1
            if len(char) > count:
                count = len(char)
        return count