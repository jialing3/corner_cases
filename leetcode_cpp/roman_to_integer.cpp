class Solution {
public:
    unordered_map<char, int> roman_to_number = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int romanToInt(string s) {
        int prior = roman_to_number.at(s[0]), total = 0, current;

        for(int i = 1; i < s.length(); ++i) {
            current = roman_to_number.at(s[i]);
            if (prior < current) {
                prior = current - prior;
            }
            else {
                total += prior;
                prior = current;
            }
        }
        total += prior;
        return total;
    }
};
