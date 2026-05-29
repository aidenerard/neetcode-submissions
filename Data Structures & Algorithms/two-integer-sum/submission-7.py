class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aDict = {}

        for i, c in enumerate(nums):
            if target - c in aDict:
                return [aDict[target - c],i]
            else:
                aDict[c] = i