"""
Runtime:            15 ms
Beats:              80.88%
Memory:             17.55 MB
Beats:              5.95%
Submission:         https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1470301812/
Time complexity:    O(n)
Topics:             #hash-table, #string, #sliding-window
Solved By:          #sliding-window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_seen = set()  # Keep track of characters seen in the current window
        longest = 0  # Store the length of the longest substring so far

        left = 0  # Left pointer of the sliding window
        for right, char in enumerate(s):
            # Move the left pointer until the character is no longer a duplicate
            while char in chars_seen:
                chars_seen.remove(s[left])  # Remove the leftmost character
                left += 1

            chars_seen.add(char)  # Add the current character to the set
            longest = max(longest, right - left + 1)  # Update the longest substring

        return longest


if __name__ == '__main__':
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
