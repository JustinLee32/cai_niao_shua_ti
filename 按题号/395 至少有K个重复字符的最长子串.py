# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2:
#
# 输入:
# s = "ababbc", k = 2
#
# 输出:
# 5
#
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。


# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         if len(s) < k or len(s) == 0:
#             return 0
#         if len(s) == k:
#             return len(s) if len(set(s)) == 1 else 0
#         temp = len(s)
#         while temp >= k:
#             for i in range(len(s)-temp+1):
#                 if self.is_ok(s[i:i+temp], k):
#                     return temp
#             temp -= 1
#         return 0
#
#     def is_ok(self, my_str, k):
#         temp_dict = {}
#         for i in range(len(my_str)):
#             if my_str[i] in temp_dict:
#                 temp_dict[my_str[i]] += 1
#             else:
#                 temp_dict[my_str[i]] = 1
#         for key, value in temp_dict.items():
#             if value >= k:
#                 continue
#             else:
#                 return False
#         return True


class Solution(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubstring("aaabbb", 3))
