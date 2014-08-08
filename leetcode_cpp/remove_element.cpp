class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (cnt > 0) {
                A[i - cnt] = A[i];
            }
            if (A[i] == elem) {
                cnt++;
            }
        }
        return n - cnt;
    }
};
