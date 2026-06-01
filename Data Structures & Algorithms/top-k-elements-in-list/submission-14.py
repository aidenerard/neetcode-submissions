class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        count = []
        for num, cnt in d.items():
            count.append([cnt, num])

        count.sort()

        out = []
        while(k > 0):
            out.append(count[-1][1])
            count.pop()
            k -= 1
        
        return out
             