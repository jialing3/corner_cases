# similar to bucket sort
# must leave at least one empty bucket
# the gap happens between the two buckets adjacent to the empty bucket

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        min_nums, max_nums, cnt = None, None, 0
        for x in nums:
            cnt += 1
            if min_nums is None:
                min_nums = x
                max_nums = x
            if x < min_nums:
                min_nums = x
            elif x > max_nums:
                max_nums = x

        num_buckets = cnt + 1 # make one more bucket than there are numbers
        buckets = [[] for _ in range(num_buckets + 1)] # one more for the boundaries
        # each bucket has a 'size' of (max_nums - min_nums) / num_buckets
        # index of any number x is floor of (x - min_nums) * num_buckets / (max_nums - min_nums)
        # keep each bucket unsorted

        for x in nums:
            ind_x = (x - min_nums) * num_buckets / (max_nums - min_nums)
            buckets[ind_x].append(x)

        max_gap = 0
        # the first and last buckets are guaranteed to be filled
        i = 1
        while i < num_buckets:
            current_bucket = buckets[i]
            if current_bucket == []:
                previous_bucket = buckets[i - 1]
                next_bucket = buckets[i + 1]
                while next_bucket == []:
                    i += 1
                    next_bucket = buckets[i + 1]
                # i still is the index for current_bucket
                current_gap = min(next_bucket) - max(previous_bucket)
                if current_gap > max_gap:
                    max_gap = current_gap
                i += 2
            else:
                i += 1

        return max_gap

        
