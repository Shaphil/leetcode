/*
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 0 ms
Memory: 6.1 MB
*/

//#include <bitset>
//#include <string>
//#include <iostream>
#include <bits/stdc++.h>


class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        std::string bin = std::bitset<64>(n).to_string();
        std::string::difference_type ones = std::count(bin.begin(), bin.end(), '1');

        return ones;
    }
};



int main()
{
    uint32_t n = 2147483647;
    Solution* solution = new Solution();
    int ones = solution->hammingWeight(n);
    std::cout << ones << std::endl;

    return 0;
}
