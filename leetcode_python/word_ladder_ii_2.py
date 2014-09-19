# BST

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict__):
        dict__ = list(dict__)
        dict__.append(end)

        dict_map = dict([(element, []) for element in dict__])
        for ind in range(len(dict__)):
            element = dict__[ind]
            for j in range(ind):
                mapped_element = dict__[j]
                if len(set(element) ^ set(mapped_element)) == 2:
                    dict_map[element].append(mapped_element)
                    dict_map[mapped_element].append(element)

        reached = False
        current = [[start]]
        while current:
            last = current
            current = []
            for combo in last:
                new_dict = list(set(dict__) - set(combo))
                current_element = combo[-1]
                for new_element in dict_map[current_element]:
                    if new_element not in combo:
                        current.append(combo + [new_element])
                        if new_element == end:
                            reached = True
            if reached == True:
                return [combo for combo in current if combo[-1] == end]
