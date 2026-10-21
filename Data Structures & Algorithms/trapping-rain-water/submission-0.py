class Solution:
    def trap(self, height: List[int]) -> int:
       
        if not height:
            return 0

        # Start pointers at the far left and far right ends
        left, right = 0, len(height) - 1
        
        # Keep track of the tallest walls seen from the left and right
        max_left = height[left]
        max_right = height[right]
        
        total_water = 0

        # Move inward until the pointers meet at the highest peak
        while left < right:
            
            # The water level is determined by the shorter of the two max walls
            if max_left < max_right:
                # Move the left pointer inward
                left += 1
                # Update the max_left wall if we found a taller one
                max_left = max(max_left, height[left])
                # Add the water trapped strictly above this specific block
                total_water += max_left - height[left]
            else:
                # Move the right pointer inward
                right -= 1
                # Update the max_right wall if we found a taller one
                max_right = max(max_right, height[right])
                # Add the water trapped strictly above this specific block
                total_water += max_right - height[right]

        return total_water