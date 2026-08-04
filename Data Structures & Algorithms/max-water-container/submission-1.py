class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            if area > most:
                most = area
            
            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        
        return most