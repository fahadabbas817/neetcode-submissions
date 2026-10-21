class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        curr_area, max_area = 0, 0 

        while left < right:
            width = right - left
            if heights[left]<heights[right]:
                length = heights[left]
                left += 1
            else:
                length = heights[right]
                right -= 1

            curr_area = length * width
            max_area = max(max_area,curr_area)
        
        return max_area
