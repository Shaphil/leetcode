/*
Runtime:    152 ms
Memory:     9.54 MB
Submission: https://leetcode.com/problems/two-sum/submissions/211518943/
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int first, last;
        int length = nums.size();
        vector<int> v;
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                if (nums[i] + nums[j] == target) {
                    first = i;
                    last = j;
                    break;
                }
            }
        }
        v.push_back(first);
        v.push_back(last);

        return v;
    }
};

int main() {
    int target = 9;
    vector<int> nums {2, 7, 11, 15};
    vector<int> result;
    Solution solution;

    result = solution.twoSum(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;

    return 0;
}