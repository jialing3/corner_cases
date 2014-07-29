// beware of unsigned int, when calculating 0 - 1.


class Solution {
public:
    void reverseWords(string &s) {
        // remove leading spaces
        while (s[0] == ' ') {
            s = s.substr(1);
        }

        // remove trailing spaces
        while (s[static_cast<int>(s.length()) - 1] == ' ') {
            s = s.substr(0, s.length() - 1);
        }

        // remove extra spaces between words
        int i = 1;
        while (i < static_cast<int>(s.length()) - 1) {
            if (s[i - 1] == ' ' && s[i] == ' ') {
                s.erase(s.begin() + i);
            }
            else {
                i += 1;
            }
        }

        // return if no space left
        bool contains_space = false;
        for (string::size_type i = 0; i < s.length(); ++i) {
            if (s[i] == ' ') {
                contains_space = true;
                break;
            }
        }

        if (!contains_space) {
            return;
        }

        // swap letter by letter
        char tmp;
        for (string::size_type i = 0; i < s.length() / 2; ++i) {
            tmp = s[i];
            s[i] = s[static_cast<int>(s.length()) - 1 - i];
            s[static_cast<int>(s.length()) - 1 - i] = tmp;
        }

        // swap again within each word
        string::size_type previous = -1;
        for (string::size_type i = 0; i <= s.length(); ++i) {
            if (s[i] == ' ' || s[i] == '\0') {
                for (string::size_type j = previous + 1; j < previous + 1 + (i - 1 - previous) / 2; ++j) {
                    tmp = s[j];
                    s[j] = s[i + previous - j];
                    s[i + previous - j] = tmp;
                }
                previous = i;
            }
        }

        return;
    }
};
