# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution:
    def minimumTotal(self, triangle) -> int:
        size = len(triangle)
        if not size:
            return 0
        judge = len(triangle[0])
        if not judge:
            return 0
        dp = [[0 for _ in range(size)] for _ in range(size)]
        dp[0][0] = triangle[0][0]
        for i in range(1, size):
            for j in range(i+1):
                if not j:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
