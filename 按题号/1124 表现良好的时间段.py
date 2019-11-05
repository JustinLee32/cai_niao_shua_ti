# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 请你返回「表现良好时间段」的最大长度。


from typing import List
#
#
# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         res = 0
#         queue = []
#         tired = 0
#         easy = 0
#         if not hours:
#             return res
#         while hours:
#             temp = hours.pop(0)
#             queue.append(temp)
#             if temp > 8:
#                 tired += 1
#             else:
#                 easy += 1
#             if tired <= easy:
#                 res = max(res, len(queue) - 1)
#                 queue = list([])
#                 tired, easy = 0, 0
#             else:
#                 res = max(res, len(queue))
#         return res


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        # 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        # 倒序扫描数组，求最大长度坡
        i = n
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans


if __name__ == '__main__':
    hours = [6, 9, 9, 9, 6]
    sol = Solution()
    print(sol.longestWPI(hours))
