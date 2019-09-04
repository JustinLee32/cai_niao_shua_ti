# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
#
# 请你返回最终形体的表面积。
#
#  
#
# 示例 1：
#
# 输入：[[2]]
# 输出：10
# 示例 2：
#
# 输入：[[1,2],[3,4]]
# 输出：34
# 示例 3：
#
# 输入：[[1,0],[0,2]]
# 输出：16
# 示例 4：
#
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 示例 5：
#
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#  
#
# 提示：
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50

# 方法：分块累加
#
# 思路
#
# 让我们试着计算 v = grid[i][j] 所贡献的表面积。
#
# 当 v > 0 时，顶面和底面的面积之和为 2。
#
# 然后，对于列 grid[i][j] 的每一侧（西，北，东，南），值为 nv 的相邻单元意味着这些方块贡献了 max(v - nv, 0) 的面积。
#
# 例如，对于 grid = [[1, 5]]，grid[0][1] 贡献的表面积是 2 + 5 + 5 + 5 + 4。
# 其中 2 来自顶部和底部；5 来自北、东、南三面；4 来自西面，其中 1 个单位被邻列覆盖。
#
# 算法
#
# 对于每个 v = grid[r][c] > 0，计算 ans += 2，对于 grid[r][c] 附近的每个相邻值 nv 还要加上 ans += max(v - nv, 0)。


class Solution:
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    # 注意这种写法！
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.surfaceArea())
