# Definition for an interval.
#class Interval:
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e


class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        return self.sort_recursive(intervals)


    def sort_recursive(self, intervals):
        if 0 <= len(intervals) <= 1:
            return intervals
        mid = len(intervals) / 2
        left_intervals = self.sort_recursive(intervals[:mid])
        right_intervals = self.sort_recursive(intervals[mid:])
        return self.merge_two(left_intervals, right_intervals)


    def merge_two(self, intervals1, intervals2):
        merged = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            if intervals1[i].start > intervals2[j].start:
                merged.append(intervals2[j])
                j += 1
            else:
                merged.append(intervals1[i])
                i += 1
        if i < len(intervals1):
            merged.extend(intervals1[i:])
        if j < len(intervals2):
            merged.extend(intervals2[j:])
        return self.merge_one(merged)


    def merge_one(self, intervals):
        merged_intervals = []
        current = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i].start > current.end:
                merged_intervals.append(current)
                current = intervals[i]
            elif intervals[i].end > current.end:
                current.end = intervals[i].end
            i += 1
        merged_intervals.append(current)
        return merged_intervals
