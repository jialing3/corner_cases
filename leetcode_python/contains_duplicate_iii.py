class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) < k:
            sliding_window = nums[:]
            sliding_window.sort()
            diff = [a - b for a, b in zip(sliding_window[:-1], sliding_window[1:])]
            return any([-t <= d <= t for d in diff])

        sliding_window = sorted(nums[:k])
        for ind in range(k, len(nums)):
            to_insert = self.insert(sliding_window, nums[ind])
            sliding_window = sliding_window[:to_insert] + [nums[ind]] + sliding_window[to_insert:]
            diff = [a - b for a, b in zip(sliding_window[:-1], sliding_window[1:])]
            if any([-t <= d <= t for d in diff]):
                return True
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
                left = mid
                break
        return left
