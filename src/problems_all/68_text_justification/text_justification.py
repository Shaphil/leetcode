"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.55 MB
Beats:              6.09%
Submission:         https://leetcode.com/problems/text-justification/submissions/1473615734/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #string, #simulation
Solved By:          #simulation
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # To store the justified lines
        current_line = []  # To store words for the current line
        current_length = 0  # Current total length of words in the line (excluding spaces)

        for word in words:
            # Check if adding the next word exceeds maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Time to justify the current line
                for i in range(maxWidth - current_length):  # Distribute spaces
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                result.append("".join(current_line))  # Combine words and spaces
                current_line = []  # Reset for the next line
                current_length = 0

            # Add the current word to the line
            current_line.append(word)
            current_length += len(word)

        # Handle the last line (left-aligned, spaces at the end)
        result.append(" ".join(current_line).ljust(maxWidth))

        return result


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    output = Solution().fullJustify(words, maxWidth)
    print(output)
