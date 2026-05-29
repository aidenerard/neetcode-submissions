class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptyList = []
        for num in nums:
            if num not in emptyList:
                emptyList.append(num)
            else:
                continue
        if len(emptyList) < len(nums):
            return True
        else:
            return False