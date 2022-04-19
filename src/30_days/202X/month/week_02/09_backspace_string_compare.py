class Solution:
    def process_string(self, s: str):
        a = list(s)
        j = 0
        for i in range(len(a)):
            if a[i] != '#':
                a[j] = a[i]
                j += 1
            else:
                if j > 0:
                    j -= 1

        b = ''
        for i in range(j):
            b += a[i]

        return b

    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.process_string(S)
        t = self.process_string(T)

        return s == t


if __name__ == "__main__":
    S = "a##c"
    T = "#a#c"
    result = Solution().backspaceCompare(S, T)
    print(result)
