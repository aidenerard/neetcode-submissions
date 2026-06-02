class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        half = []

        if len(nums) == 0:
            return 0

        for num in nums:
            d[num] = 1
        
        for n in d:
            start = n
            while n + 1 in d:
                d[start] += 1
                n += 1
        
        return max(d.values())
                