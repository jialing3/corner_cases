def find_start_pos(A, target):
    if len(A) == 1:
        return 0 if target == A[0] else None

    mid = (len(A) - 1) / 2 # (start + end) / 2

    if A[mid] == target:
        return find_start_pos(A[:mid + 1], target)
    elif A[mid] < target:
        tmp = find_start_pos(A[mid + 1:], target)
        return None if tmp is None else tmp + mid + 1
    else: # >
        return find_start_pos(A[:mid], target)


if __name__ == '__main__':
    A = [1, 1, 2, 2, 3, 3, 4, 4, 4]
    print A
    for target in range(6):
        print target, find_start_pos(A, target)
