class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0 or t < 0:
            return False

        if len(nums) < k:
            sliding_window = nums[:]
            sliding_window.sort()
            diff = [a - b for a, b in zip(sliding_window[:-1], sliding_window[1:])]
            return any([-t <= d <= t for d in diff])


        sliding_window = sorted(nums[:k])
        for ind in range(k, len(nums)):
            is_found, position_to_insert = self.insert(sliding_window, nums[ind])
            if is_found:
                return True
            else:
                if position_to_insert == 0:
                    if abs(nums[ind] - sliding_window[position_to_insert]) <= t:
                        return True
                elif position_to_insert == len(sliding_window):
                    if abs(nums[ind] - sliding_window[position_to_insert - 1]) <= t:
                        return True
                elif abs(nums[ind] - sliding_window[position_to_insert - 1]) <= t or abs(nums[ind] - sliding_window[position_to_insert]) <= t:
                    return True
            sliding_window.insert(position_to_insert, nums[ind])
            sliding_window.remove(nums[ind - k])
        else:
            return False


    def insert(self, lst, target):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if lst[mid] > target:
                right = mid - 1
            elif lst[mid] < target:
                left = mid + 1
            else:
                return (True, mid)
        return (False, left)
