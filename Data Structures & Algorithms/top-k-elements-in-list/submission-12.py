class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        newList = []
        for i in range(len(nums) + 1):
            newList.append([])

        # [[] [] [] [] [] [] []]

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # count = {1: 3, 2: 2, 3: 1}

        for num, val in count.items():
            newList[val].append(num)
        
        # newList = [[], [3], [2], [1], [], [], []]

        finalList = []
        for numList in newList[::-1]:
            for num in numList:
                finalList.append(num)
                if len(finalList) == k:
                    return finalList

        # k = 2
        # finalList = [1, 2]
