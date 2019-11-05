# 给你一个整数数组
# arr
# 和一个整数
# difference，请你找出
# arr
# 中所有相邻元素之间的差等于给定
# difference
# 的等差子序列，并返回其中最长的等差子序列的长度。
#
#
#
# 示例
# 1：
#
# 输入：arr = [1, 2, 3, 4], difference = 1
# 输出：4
# 解释：最长的等差子序列是[1, 2, 3, 4]。
# 示例
# 2：
#
# 输入：arr = [1, 3, 5, 7], difference = 1
# 输出：1
# 解释：最长的等差子序列是任意单个元素。
# 示例
# 3：
#
# 输入：arr = [1, 5, 7, 8, 5, 3, 4, 2, 1], difference = -2
# 输出：4
# 解释：最长的等差子序列是[7, 5, 3, 1]。
#
#
# 提示：
#
# 1 <= arr.length <= 10 ^ 5
# -10 ^ 4 <= arr[i], difference <= 10 ^ 4

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 0
        res_dic = {}
        res_dic[arr[0]] = 1
        for i in range(len(arr)):
            if arr[i] - difference in res_dic:
                res_dic[arr[i]] = res_dic[arr[i] - difference] + 1
            else:
                res_dic[arr[i]] = 1
        for key, val in res_dic.items():
            res = max(res, val)
        return res
        #
        # dp = [1 for _ in range(len(arr))]
        # for i in range(1, len(arr)):
        #     for j in range(i, -1, -1):
        #         if arr[i] - arr[j] == difference:
        #             dp[i] = dp[j] + 1
        #             break
        # return max(dp)


if __name__ == '__main__':
    arr = [8, 7, 6, 5, 3, 1, 6, 4, 2, 0]
    difference = -2
    sol = Solution()
    print(sol.longestSubsequence(arr, difference))
