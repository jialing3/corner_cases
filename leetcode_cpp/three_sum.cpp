class Solution {
public:

    vector<vector<int> > threeSum(vector<int> &num) {
        sort(num.begin(), num.end());

        int j, k;
        vector<vector<int> > solutions;
        set<vector<int> > sol_set;
        vector<int> int_vec(3);

        for (int i = 0; i < num.size(); ++i) {
            if (i > 0 && num[i - 1] == num[i]) {
                continue;
            }
            j = i + 1;
            k = num.size() - 1;
            while (j < k) {
                if (num[i] + num[j] + num[k] == 0) {
                    int_vec[0] = num[i];
                    int_vec[1] = num[j];
                    int_vec[2] = num[k];
                    sol_set.insert(int_vec);
                    int_vec.empty();
                    j += 1;
                    k -= 1;
                }
                else if (num[i] + num[j] + num[k] > 0) {
                    k -= 1;
                }
                else {
                    j += 1;
                }
            }
        }

        solutions.assign(sol_set.begin(), sol_set.end());

        return solutions;
    }

};
