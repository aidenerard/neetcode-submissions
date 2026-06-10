class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            low = min(heights[left], heights[right])
            if low * (right - left) > water:
                water = low * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return water