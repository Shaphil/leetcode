import os
from pprint import pprint as pp
from typing import List

import psutil

from utils import timer, memory_usage


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            data = ''.join(sorted(word))
            if data in anagrams:
                anagrams[data].append(word)
            else:
                anagrams[data] = [word]

        return list(anagrams.values())


@memory_usage
@timer
def main():
    data = ["and", "dan"]
    anagrams = Solution().groupAnagrams(data)
    pp(anagrams)


if __name__ == "__main__":
    main()
