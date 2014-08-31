# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):

        def get_slope(p1, p2):
            if (p1.x, p1.y) == (p2.x, p2.y):
                return 'Same'
            elif p1.x == p2.x:
                return 'Inf'
            else:
                return 1. * (p2.y - p1.y) / (p2.x - p1.x)


        if len(points) < 3:
            return len(points)
        max_count = 0
        for i in range(len(points)):
            line_count = {'base': 0} # for edge cases with only overlapping points
            for j in range(len(points)):
                if i == j:
                    continue
                else:
                    slope = get_slope(points[i], points[j])
                    if slope not in line_count:
                        line_count[slope] = 0
                    line_count[slope] += 1
            if 'Same' in line_count:
                same = line_count.pop('Same')
                for slope in line_count:
                    line_count[slope] += same
            max_count = max(max_count, max(line_count.values()) + 1)


        return max_count
