# BST

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dict.add(end)
        reached = False
        current = [[start]]
        while current:
            last = current
            current = []
            for combo in last:
                new_dict = list(set(dict) - set(combo))
                current_element = combo[-1]
                for new_element in new_dict:
                    if len(set(new_element) ^ set(current_element)) == 2:
                        current.append(combo + [new_element])
                        if new_element == end:
                            reached = True
            if reached == True:
                return [combo for combo in current if combo[-1] == end]
