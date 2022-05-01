class Solution:
    def get_string(self, text):
        chars = []
        for char in text:
            if char == '#':
                if chars:
                    chars.pop()
            else:
                chars.append(char)

        text = ''.join(chars)
        return text

    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.get_string(s)
        t = self.get_string(t)

        return s == t


# Old Solution
# class Solution:
#     def process_string(self, s: str):
#         a = list(s)
#         j = 0
#         for i in range(len(a)):
#             if a[i] != '#':
#                 a[j] = a[i]
#                 j += 1
#             else:
#                 if j > 0:
#                     j -= 1

#         b = ''
#         for i in range(j):
#             b += a[i]

#         return b

#     def backspaceCompare(self, S: str, T: str) -> bool:
#         s = self.process_string(S)
#         t = self.process_string(T)

#         return s == t


if __name__ == '__main__':    
    s = "y#fo##f"
    t = "y#f#o##f"
    solution = Solution().backspaceCompare(s, t)
    print(solution)
