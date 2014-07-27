class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        unordered_map<int, int> map;
        int counter = 1, difference, ind1, ind2, tmp;
        for (vector<int>::iterator it = numbers.begin(); it != numbers.end(); ++it) {
            map[*it] = counter++;
        }
        counter = 1;
        for (vector<int>::iterator it = numbers.begin(); it != numbers.end(); ++it) {
            difference = target - *it;
            if (map.count(difference) != 0) {
                ind1 = counter;
                ind2 = map[difference];
                if (ind1 != ind2) {
                    if (ind1 > ind2) {
                        tmp = ind1;
                        ind1 = ind2;
                        ind2 = tmp;
                    }
                    return vector<int> {ind1, ind2};
                }
            }
            ++counter;
        }
    }
};
