class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry = 0
        c = ''
        position = -1
        while max(len(a), len(b)) >= abs(position):
            current_a = 0 if len(a) < abs(position) else int(a[position])
            current_b = 0 if len(b) < abs(position) else int(b[position])
            tmp_sum = current_a + current_b + carry
            carry = tmp_sum / 2
            c = str(tmp_sum % 2) + c
            position -= 1
        # key! carry-over of the largest digit
        if carry:
            c = str(carry) + c
        return c
