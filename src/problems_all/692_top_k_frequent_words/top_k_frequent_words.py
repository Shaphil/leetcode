"""
Runtime:            3 ms
Beats:              52.70%
Memory:             17.50 MB
Beats:              8.84%
Submission:         https://leetcode.com/problems/top-k-frequent-words/submissions/1477088376/
Time complexity:    `O(n log n + k log n)` = `O(n log n)`, assuming k is significantly smaller than n.
                    * Building the heap: O(n log n), where n is the number of words.
                    * Extracting the top k elements: O(k log n)
Space complexity:   O(n)
Topics:             #hash-table, #string, #trie, #sorting, #heap (Priority Queue), #bucket-sort, #counting
Solved By:          #heap
"""

import heapq  # Use a heapq for potentially faster top k selection
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        # Create a min-heap based on frequency (descending)
        min_heap = [(-count, word) for word, count in counter.items()]
        heapq.heapify(min_heap)

        # Extract top k elements (words with highest frequencies)
        top_words = []
        for _ in range(k):
            count, word = heapq.heappop(min_heap)
            top_words.append(word)

        return top_words


if __name__ == '__main__':
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    result = Solution().topKFrequent(words, k)
    print(result)
