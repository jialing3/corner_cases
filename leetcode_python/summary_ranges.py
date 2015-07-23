class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        output = []
        current_beginning = None
        for ind, num in enumerate(nums):
            if ind == 0:
                current_beginning = num
            else:
                if num - nums[ind - 1] > 1:
                    if current_beginning is None or nums[ind - 1] == current_beginning: #key
                        output.append(str(nums[ind - 1]))
                    else:
                        output.append(str(current_beginning) + '->' + str(nums[ind - 1]))
                    current_beginning = num
        if len(nums):
            if num == current_beginning:
                output.append(str(num))
            else:
                output.append(str(current_beginning) + '->' + str(num))
        return output
