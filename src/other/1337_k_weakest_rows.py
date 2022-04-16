from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = []
        for idx, row in enumerate(mat):
            data.append((idx, row.count(1)))

        sorted_data = sorted(data, key=lambda tup: tup[1])
        result = []
        for i, val in enumerate(sorted_data):
            if i < k:
                result.append(val[0])
            else:
                break

        return result


def main():
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3
    result = Solution().kWeakestRows(mat, k)
    print(result)


if __name__ == "__main__":
    main()
