def find_start_pos(A, target):
    if len(A) == 0:
        return None
    elif [target] == A:
        return 0
    elif len(A) == 1 and target != A[0]:
        return None

    mid = (len(A) - 1) / 2

    if A[mid] == target:
        return find_start_pos(A[:mid + 1], target)
    elif A[mid] < target:
        tmp = find_start_pos(A[mid + 1:], target)
        return None if tmp is None else tmp + mid + 1
    else: # >
        return find_start_pos(A[:mid], target)


if __name__ == '__main__':
    A = [1, 1, 2, 2, 3, 3, 4, 4, 4]
    target = 3
    print A, target, find_start_pos(A, target)
