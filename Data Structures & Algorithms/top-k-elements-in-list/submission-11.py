class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        # freq = [[] [] [] [] [] []]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for n, c in count.items():
            freq[c].append(n)

        # freq = [[] [1] [2] [3] [] [] []]

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result