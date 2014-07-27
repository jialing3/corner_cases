class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        number_to_index = {}
        for ind, number in enumerate(num):
            number_to_index[number] = ind
        for ind, number in enumerate(num):
            difference = target - number
            if difference in number_to_index:
                if ind != number_to_index[difference]:
                    return sorted((ind + 1, number_to_index[difference] + 1))
