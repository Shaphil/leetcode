class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexes = []
        is_found = True
        copy = t
        count = 0
        padding = 0
        for c in s:
            try:
                idx = copy.index(c)
                indexes.append(idx + padding)
                copy = copy[idx + 1 :]
                padding = indexes[count]
                count += 1
            except ValueError:
                is_found = False
                break

        print(indexes)
        if count < len(s):
            is_found = False

        # if is_found and len(t) >= len(indexes):
        #     prev = -1
        #     for i in indexes:
        #         if i < prev:
        #             is_found = False
        #             break
        #         prev = i

        return is_found


if __name__ == "__main__":
    s = "twn"
    t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"

    solution = Solution()
    result = solution.isSubsequence(s, t)
    print(result)
