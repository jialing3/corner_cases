# two pointer sweep
# shorter line is relevant for volume, so always move the pointer for the shorter line

class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left < right:
            current_volume = min(height[left], height[right]) * (right - left) # height times width
            max_volume = max(max_volume, current_volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_volume
