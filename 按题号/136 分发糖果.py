# -*- coding utf-8 -*-
# creat on Sept 13th

# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？
#
# 示例 1:
#
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 示例 2:
#
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
#

# cache = []
# if n <= 1:
#     print(1)
# else:
#     for i in range(n):
#         if not cache:
#             cache.append(scores[i])
#         elif scores[i] <= cache[-1]:
#             cache.append(scores[i])
#         elif scores[i] > cache[-1]:
#             res += calc_sum(cache)
#             cache = []
#             cache.append(scores[i])
# print(res)
#
#
# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         n = len(ratings)
#         if not n:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             cache = []
#             res = 0
#             for i in range(n):
#                 if not cache:
#                     cache.append(ratings[i])
#                 elif ratings[i] <= cache[-1]:
#                     cache.append(ratings[i])
#                 elif ratings[i] > cache[-1]:
#                     res += ratings(cache, last)
#                     cache = []
#                     cache.append(ratings[i])
#                     last =
#
#
#     def calc_sum(self, cache, last):
#         ans = 0
#         now = 0
#         num = 0
#         for i in range(len(cache) - 1, 0, -1):
#             if not now:
#                 num += 1
#                 ans += num
#                 now = cache[i]
#             else:
#                 if cache[i] > now:
#                     num += 1
#                     ans += num
#                     now = cache[i]
#                 elif cache[i] == now:
#                     ans += num
#         if cache[0] > now:
#             ans += max(last, num) + 1
#         elif cache[0] == now:
#             ans += max(last+1, now)
#         return ans
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.candy([1, 2, 2]))


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count