class Solution {
public:
    void sortColors(int A[], int n) {

        int zero = 0, two = n - 1, i = 0;
        while (i <= two) {
            if (A[i] == 2) {
                std::swap(A[i], A[two]);
                --two;
            }
            if (A[i] == 0) {
                std::swap(A[i], A[zero]);
                ++zero;
                ++i;
                continue;
            }
            if (A[i] == 1) {
                ++i;
            }
        }
    }
};
