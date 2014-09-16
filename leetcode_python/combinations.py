class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        current = [set()]
        for level in range(k):
            last = current
            current = []
            for node in last:
                for element in range(1, n + 1):
                    if element not in node:
                        if (len(node) > 0 and element > max(node)) or len(node) == 0:
                            new_node = set(list(node) + [element])
                            current.append(new_node)
        return [sorted(node) for node in current]
            
