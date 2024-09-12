/*
Runtime:    9 ms
Memory:     14.34 MB
Submission: https://leetcode.com/problems/two-sum/submissions/1385368859/
*/

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> nums_to_index;
        std::vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (nums_to_index.count(complement)) {
                result.push_back(nums_to_index[complement]);
                result.push_back(i);
                return result;
            }
            nums_to_index[nums[i]] = i;
        }
        return result;
    }
};

int main() {
    int target = 6;
    vector<int> nums {3, 2, 4};
    vector<int> result;
    Solution solution;

    result = solution.twoSum(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;

    return 0;
}