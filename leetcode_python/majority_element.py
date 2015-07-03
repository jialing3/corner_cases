class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums): # time is O[n] and space is O[n]
        cnt = {}
        size = len(nums)
        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1
            if cnt[num] > size / 2:
                return num


    def majorityElement_recursive(self, nums): # time is O[n logn], space is O[1]
        if len(nums) == 1:
            return nums[0]
        middle = len(nums) / 2
        left_majority = self.majorityElement_recursive(nums[:middle])
        right_majority = self.majorityElement_recursive(nums[middle:])
        if left_majority == right_majority:
            return left_majority
        else:
            cnt_left = 0
            cnt_right = 0
            for num in nums:
                if num == left_majority:
                    cnt_left += 1
                elif num == right_majority:
                    cnt_right += 1
            return left_majority if cnt_left > cnt_right else right_majority
