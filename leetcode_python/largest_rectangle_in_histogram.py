# push onto stack (to be processed later) when ascending or flat
# pop off stack till the remaining is smaller than current
# calculate areas when popping

# handle the local peaks on the fly

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):

        max_area = 0
        if not height:
            return max_area

        stack = [] # keep inds
        height = [0] + height # makes sure the first element is popped off
        height.append(0) # makes sure the last pass of non-descending stack gets popped off

        for i, y in enumerate(height):
            while stack and height[stack[-1]] >= y:
                popped_i = stack.pop()
                max_area = max(max_area, height[popped_i] * (i - stack[-1] - 1 if stack else 1))
            stack.append(i)

        return max_area
