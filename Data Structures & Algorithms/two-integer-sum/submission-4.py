class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newList = nums[:]
        for i in range(len(nums)):
            for j in range(len(newList)):
                if nums[i] + newList[j] == target:
                    if i != j:
                        return [i,j]
                    else:
                        continue
                else:
                    continue