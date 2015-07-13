# pivot and toss away half

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if k == 1 and len(nums) == 1:
            return nums[0]
        else:
            pivot = nums.pop()
            left = []
            right = []
            left_size = 0
            right_size = 0
            for n in nums:
                if n < pivot:
                    left.append(n)
                    left_size += 1
                else:
                    right.append(n)
                    right_size += 1
            if k == right_size + 1:
                return pivot
            elif k <= right_size:
                return self.findKthLargest(right, k)
            else: # k > right_size + 1
                return self.findKthLargest(left, k - right_size - 1)




            
