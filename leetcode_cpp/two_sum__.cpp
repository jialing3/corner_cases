// O(n) time, O(n) space
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



// O(nlgn) time, O(n) space
class Solution {
public:
    struct Node
    {
        int val;
        int index;
        Node(int pVal, int pIndex):val(pVal), index(pIndex){}
    };
    static bool compare(const Node &left, const Node &right)
    {
        return left.val < right.val;
    }
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<Node> elements;
        for (int i=0; i<nums.size(); i++)
        {
            elements.push_back(Node(nums[i], i));
        }
        std::sort(elements.begin(), elements.end(), compare);
        int start = 0, end = nums.size()-1;
        vector<int> result;
        while (start < end)
        {
            int sum = elements[start].val + elements[end].val;
            if (sum == target)
            {
                if (elements[start].index<elements[end].index)
                {
                    result.push_back(elements[start].index+1);
                    result.push_back(elements[end].index+1);
                }
                else
                {
                    result.push_back(elements[end].index+1);
                    result.push_back(elements[start].index+1);
                }
                break;
            }
            else if (sum < target)
            {
                start++;
            }
            else
            {
                end--;
            }
        }
        return result;
    }
};
