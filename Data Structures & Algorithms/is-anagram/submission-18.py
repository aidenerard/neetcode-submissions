class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myDict = {}
        for c in s:
            if not c in myDict:
                myDict[c] = 1
            else:
                myDict[c] += 1
        # {'r': 2, 'a': 2, 'c': 2, 'e': 1}

        for a in t:
            if a in myDict and myDict[a] > 0:
                myDict[a] -= 1
            else:
                return False
        return True