# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not k or not n:
            return []

        res = []

        def dfs(k, n, tmp, start):
            if n == 0 and k == 0:
                res.append(tmp[:])
                return
            if k <= 0 or n <= 0:
                return

            for i in range(start, 10):
                tmp.append(i)
                dfs(k - 1, n - i, tmp, i + 1)
                tmp.pop()

        dfs(k, n, [], 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(3, 9))