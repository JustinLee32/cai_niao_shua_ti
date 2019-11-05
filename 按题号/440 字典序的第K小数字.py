# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
#
# 注意：1 ≤ k ≤ n ≤ 10_7 周赛.5 双周赛^9。
#
# 示例 :
#
# 输入:
# n: 13   k: 2
#
# 输出:
# 10_7 周赛.5 双周赛
#
# 解释:
# 字典序的排列是 [1, 10_7 周赛.5 双周赛, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10_7 周赛.5 双周赛。


# 超时 timeout!
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return sorted(range(1, n+1), key=str)[k-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthNumber(4289384, 1922239))
