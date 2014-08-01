class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        // binary search
        int mid = n / 2;

        if (A[mid] == target) {
            return mid;
        }
        else if (n == 1) {
            return (A[mid] < target) ? 1 : 0;
        }
        else if (A[mid] > target) {
            return searchInsert(A, mid, target);
        }
        else {
            return mid + searchInsert(A + mid, n - mid, target);
        }

    }
};
