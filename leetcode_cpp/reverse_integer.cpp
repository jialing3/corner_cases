class Solution {
public:
    int reverse(int x) {
        string x_str = to_string(x);
        int initial_pos = (x_str[0] == '-') ? 1 : 0;
        char tmp;

        for (int i = initial_pos; i < (x_str.size() + initial_pos) / 2; ++i) {
            tmp = x_str[i];
            x_str[i] = x_str[x_str.size() + initial_pos - 1 - i];
            x_str[x_str.size() + initial_pos - 1 - i] = tmp;
        }

        return stoi(x_str);
    }
};
