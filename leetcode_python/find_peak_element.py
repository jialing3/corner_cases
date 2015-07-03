# binary search
# MIT 6.006

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        return self.find_peak_element(nums, 0, len(nums) - 1)

    def find_peak_element(self, nums, beginning, end):
        middle = beginning + (end - beginning) / 2
        if (middle == beginning or nums[middle] > nums[middle - 1]) and (middle == end or nums[middle] > nums[middle + 1]):
            # max or edge
            return middle
        elif middle > beginning and nums[middle] < nums[middle - 1]:
            # recurse left
            return self.find_peak_element(nums, beginning, middle - 1)
        elif middle < end and nums[middle] < nums[middle + 1]:
            # recurse right
            return self.find_peak_element(nums, middle + 1, end)
