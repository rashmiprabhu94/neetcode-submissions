class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left   

            if heights[left] > heights[right]:
                area = heights[right] * length
                right -= 1
            else:
                area = heights[left] * length
                left += 1

            result = max(area, result)

        return result