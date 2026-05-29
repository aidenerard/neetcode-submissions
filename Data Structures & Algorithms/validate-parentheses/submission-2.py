class Solution:
    def isValid(self, s: str) -> bool:
        aList = []
        aDict = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in aDict:
                if aList and aDict[char] == aList[-1]:
                    aList.pop()
                else:
                    return False
            else:
                aList.append(char)
        if not aList:
            return True
        else:
            return False

        