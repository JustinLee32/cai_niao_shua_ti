# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
#
# 如果有多个目标子集，返回其中任何一个均可。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2] (当然, [1,3] 也正确)
# 示例 2:
#
# 输入: [1,2,4,8]
# 输出: [1,2,4,8]


class Solution:
    def largestDivisibleSubset(self, nums: list) -> list:
        if not nums:
            return []
        nums.sort()
        dp = [[0, []] for _ in range(len(nums))]
        dp[0] = (1, [nums[0]])
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j]:
                    if dp[i][0] == 0:
                        dp[i][0] = 1
                        dp[i][1] = [nums[i]]
                else:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = list(dp[j][1])
                        dp[i][1].append(nums[i])
                    elif dp[j][0] + 1 <= dp[i][0]:
                        continue
        dp.sort(key=lambda x: x[0])
        return dp[-1][1]


#########################################################
## 以下写法特别关注max(list1, list2, list3, key=len)的写法 ##
#########################################################
# class Solution(object):
#     def largestDivisibleSubset(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#
#         if not nums: return nums
#         if len(nums) == 1: return nums
#         l = len(nums)
#         nums.sort()
#
#         dp = [[i] for i in nums]
#
#         for i in range(1, l):
#             for j in range(i - 1, -1, -1):
#                 if not nums[i] % nums[j]:
#                     dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)
#
#         return max(dp, key=len)

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset([3, 4, 16, 8]))
