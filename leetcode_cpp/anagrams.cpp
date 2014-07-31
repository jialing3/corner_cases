class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {

        unordered_map<string, vector<string> > strs_map;

        for (int i = 0; i < strs.size(); ++i) {
            string str = strs[i];
            string str_key = str;
            sort(str_key.begin(), str_key.end());
            if (strs_map.count(str_key) == 0) {
                strs_map[str_key] = {};
            }
            strs_map[str_key].push_back(str);
        }

        vector<string> solutions;

        for (auto kv : strs_map) {
            if (kv.second.size() > 1) {
                solutions.insert(solutions.end(), kv.second.begin(), kv.second.end());
            }
        }

        return solutions;
    }
};
