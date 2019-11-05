# 给出一个字符串
# s
# 和一个整数
# k，请你帮忙判断这个字符串是不是一个「K
# 回文」。
#
# 所谓「K
# 回文」：如果可以通过从字符串中删去最多
# k
# 个字符将其转换为回文，那么这个字符串就是一个「K
# 回文」。
#
#
#
# 示例：
#
# 输入：s = "abcdeca", k = 2
# 输出：true
# 解释：删除字符 “b” 和 “e”。
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s
# 中只含有小写英文字母
# 1 <= k <= s.length


# class Solution:
#     def isValidPalindrome(self, s: str, k: int) -> bool:
#         self.memory = [[[0 for _ in range(k+1)] for _ in range(len(s))] for _ in range(len(s))]
#         self.ans = False
#         if len(s) == 1:
#             return True
#         if len(s) == 2:
#             return True if s[0] == s[1] else False
#         else:
#             def _recursion(s, k, left, right):
#                 if k < 0:
#                     return
#                 if self.ans:
#                     self.memory[left][right][k] = 1
#                     return
#                 if left >= right:
#                     self.ans = True
#                     self.memory[left][right][k] = 1
#                     return
#                 if self.memory[left][right][k]:
#                     return
#                 if s[left] == s[right]:
#                     self.memory[left][right][k] = 1
#                     _recursion(s, k, left + 1, right - 1)
#                 elif s[left] != s[right]:
#                     self.memory[left][right][k] = 1
#                     if not k:
#                         return
#                     else:
#                         _recursion(s, k - 1, left + 1, right)
#                         _recursion(s, k - 1, left, right - 1)
#
#             _recursion(s, k, 0, len(s) - 1)
#             return self.ans


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        t = s[::-1]
        L = len(s)
        dp = [[0] * (L + 1) for _ in range(L + 1)]

        for i in range(1, L + 1):
            for j in range(1, L + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[L][L] + k >= L


if __name__ == '__main__':
    s = "dbabdadcbbcbacaabbbaaabdbdbcdacdcbadbacacaccdcdbabcabcbcbbcadbbbdadacdbaadaadcbcddbabddbbcacbccbddbcccbaadccddccacacadcbccbbccbdbadccbcbdbcaacbdadbdbbbdccabdbcbadacabbaadabddacaacccbccddcbddcddbddcbabbaccbdcbabbdcdacaddcdabdbbdaaccabdabbbcbbbaccdacccccdbcbaaddddbdabbbddbcbdaddddcabadbccbbaccbdbccacacbbdbdbcbccdddbabdbbadbdcdcbaabcaabdcacdcbb"
    k = 216
    sol = Solution()
    print(sol.isValidPalindrome(s, k))

