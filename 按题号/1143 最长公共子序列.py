# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m, n = len(text1), len(text2)
#         dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if text1[j - 1] == text2[i - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#         return dp[n][m]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memory = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        def _recursion(text1: str, text2: str, probe1: int, probe2: int):
            if self.memory[probe1][probe2] >= 0:
                return self.memory[probe1][probe2]
            if probe1 == len(text1) or probe2 == len(text2):
                self.memory[probe1][probe2] = 0
                return 0
            if text1[probe1] == text2[probe2]:
                self.memory[probe1][probe2] = _recursion(text1, text2, probe1 + 1, probe2 + 1) + 1
                return self.memory[probe1][probe2]
            elif text1[probe1] != text2[probe2]:
                self.memory[probe1][probe2] = max(_recursion(text1, text2, probe1 + 1, probe2), _recursion(text1, text2, probe1, probe2 + 1))
                return self.memory[probe1][probe2]

        return _recursion(text1, text2, 0, 0)


if __name__ == '__main__':
    text1 = "bl"
    text2 = "yby"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))
