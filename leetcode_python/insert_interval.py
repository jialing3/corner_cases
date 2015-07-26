# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]

        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if intervals[mid].start < newInterval.start:
                left = mid + 1
            elif intervals[mid].start > newInterval.start:
                right = mid - 1
            else: # ==
                left = mid # key
                break
        ind_to_insert_start = left

        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if intervals[mid].end < newInterval.end:
                left = mid + 1
            elif intervals[mid].end > newInterval.end:
                right = mid - 1
            else: # ==
                left = mid # key
                break
        ind_to_insert_end = left


        connected_to_the_front = (intervals[ind_to_insert_start - 1].end >= newInterval.start) if ind_to_insert_start > 0 else False # no front if 0
        connected_to_the_back = (intervals[ind_to_insert_end].start <= newInterval.end) if ind_to_insert_end < len(intervals) else False # no back if len(intervals)

        front = intervals[:ind_to_insert_start] if not connected_to_the_front else intervals[:ind_to_insert_start - 1]
        back = intervals[ind_to_insert_end:] if not connected_to_the_back else intervals[ind_to_insert_end + 1:]

        middle_start = newInterval.start if not connected_to_the_front else intervals[ind_to_insert_start - 1].start
        middle_end = newInterval.end if not connected_to_the_back else intervals[ind_to_insert_end].end
        middle = [Interval(middle_start, middle_end)]

        return front + middle + back
