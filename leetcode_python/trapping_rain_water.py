# water level is min(left_max, right_max) at position i

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        current_max = -1
        left_max = []
        for x in height:
            if x > current_max:
                current_max = x
            left_max.append(current_max)
        current_max = -1
        area = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > current_max:
                current_max = height[i]
            area += min(current_max, left_max[i]) - height[i]
        return area
            
