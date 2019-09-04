# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false


class Solution:
    def __init__(self):
        self.flag = 0
        self.memo = set()

    def wordBreak(self, s: str, wordDict: list) -> bool:
        temp_list = []
        temp_list += self._compare(wordDict, s, 0)
        if not temp_list:
            return False
        elif self.flag == 1:
            return True
        else:
            while temp_list:
                word, probe = temp_list.pop()
                if probe in self.memo:
                    continue
                temp_list += self._compare(wordDict, s, probe)
                if self.flag == 1:
                    return True
            return False

    def _compare(self, wordDict, string, probe):
        res = []
        self.memo.add(probe)
        for word in wordDict:
            if len(word) > len(string) - probe:
                continue
            elif word == string[probe:probe+len(word)]:
                res.append((word, probe + len(word)))
                if probe + len(word) == len(string):
                    self.flag = 1
        return res

# class Solution:
#     def wordBreak(self, s, wordDict):
#         dp = [0 for i in range(len(s))]
#         temp = self._compare(wordDict, s, 0)
#         if temp:
#             for num in temp:
#                 dp[num-1] = 1
#         else:
#             return False
#         for i in range(1, len(s)):
#             if dp[i]:
#                 continue
#             if dp[len(s)-1]:
#                 return True
#             else:
#                 for j in range(i+1):
#                     if dp[j] == 0:
#                         continue
#                     else:
#                         temp = self._compare(wordDict, s, j)
#                         if temp:
#                             for num in temp:
#                                 dp[num-1] = 1
#                         else:
#                             continue
#         if dp[len(s)-1] == 1:
#             return True
#         else:
#             return False
#
#     def _compare(self, wordDict, string, probe):
#         res = []
#         for word in wordDict:
#             if len(word) > len(string) - probe:
#                 continue
#             elif word == string[probe:probe+len(word)]:
#                 res.append(probe + len(word))
#         return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                        , ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    # print(sol.wordBreak("leetcode", ["leet", "code"]))