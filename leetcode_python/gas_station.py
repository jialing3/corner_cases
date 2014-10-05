class Solution:
    def get_next(self, i, gas):
        if i == len(gas) - 1:
            return 0
        else:
            return i + 1

    def get_last(self, i, gas):
        if i == 0:
            return len(gas) - 1
        else:
            return i - 1

    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0:
            return -1
        left, right, current = 0, 0, 0
        net = gas[current] - cost[current]
        while left != self.get_next(right, gas):
            if net < 0: # go back till net is non-negative
                left = self.get_last(left, gas)
                current = left
            else:
                right = self.get_next(right, gas)
                current = right
            net += gas[current] - cost[current]
        if net < 0:
            return -1
        else:
            return left
                
