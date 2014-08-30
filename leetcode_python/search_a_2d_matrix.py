class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        def search_row(matrix, target):
            n_rows = len(matrix)
            if n_rows == 0:
                return [] # empty row
            mid_row = matrix[n_rows / 2]
            if mid_row[0] <= target <= mid_row[-1]:
                return mid_row
            elif mid_row[0] > target:
                return search_row(matrix[:(n_rows / 2)], target)
            else: # mid_row[-1] < target
                return search_row(matrix[(n_rows / 2 + 1):], target)


        def search_element(row, target):
            n_elements = len(row)
            if n_elements == 0:
                return False
            mid_element = row[n_elements / 2]
            if mid_element == target:
                return True
            elif mid_element > target:
                return search_element(row[:(n_elements / 2)], target)
            else: # mid_element < target
                return search_element(row[(n_elements / 2 + 1):], target)

        target_row = search_row(matrix, target)
        return search_element(target_row, target)
