class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        final = []

        for word in strs:
            arr = 26 * [0]
            for c in word:
                num = ord(c) - ord('a')
                arr[num] += 1

            tup = tuple(arr)

            if tup not in d:
                d[tup] = [word]
            else:
                d[tup].append(word)

        for vals in d.values():
            final.append(vals)
        
        return final