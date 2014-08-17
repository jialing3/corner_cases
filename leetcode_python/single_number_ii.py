class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones, twos = 0, 0               # keeping count of number of appearance mod 3
        for x in A:
            twos |= ones & x            # common set bits in x and ones, OR with twos
            ones ^= x                   # XOR of x with ones
            not_threes = ~(ones & twos) # Common set bits in ones and two are those appearing 3rd time
            ones &= not_threes
            twos &= not_threes
        return ones
