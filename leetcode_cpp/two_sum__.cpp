class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mapping;
        vector<int> result;
        for (int i=0; i<nums.size(); i++)
        {
            mapping[nums[i]] = i;
        }
        for (int i=0; i<nums.size(); i++)
        {
            int searched = target - nums[i];
            if (mapping.find(searched) != mapping.end() && mapping[searched] != i)
            {
                result.push_back(i+1);
                result.push_back(mapping[searched]+1);
                break;
            }
        }
        return result;
    }
};
