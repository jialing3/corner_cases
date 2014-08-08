class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int number_of_duplicates = 0;
        for (int i = 1; i < n; ++i) {
            if (A[i] == A[i - 1]) {
                number_of_duplicates += 1;
            }
            else if (number_of_duplicates > 0) {
                A[i - number_of_duplicates] = A[i];
            }
        }
        return n - number_of_duplicates;
    }
};
