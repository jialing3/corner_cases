class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if min(E, G) >= max(A, C) or max(E, G) <= min(A, C) or min(F, H) >= max(B, D) or max(F, H) <= min(B, D):
            return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F)

        else:
            return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F) - self.diff_of_middle_two(A, C, E, G) * self.diff_of_middle_two(B, D, F, H)

    def diff_of_middle_two(self, a, b, c, d):
        ends = sorted([a, b, c, d])[1:3]
        return abs(ends[0] - ends[1])
