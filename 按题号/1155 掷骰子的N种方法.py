# 这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
# 我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
# 如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10_7 周赛.5 双周赛^9 + 7 后返回。


class Solution:
    def numRollsToTargetRecursion(self, d: int, f: int, target: int) -> int:
        self.ans = 0

        def _recursion(num, face, he):
            if not he and not num:
                self.ans += 1
            elif he <= 0 or not num:
                return
            elif he > 0 and num:
                for number in range(1, f + 1):
                    _recursion(num - 1, face, he - number)

        _recursion(d, f, target)
        return self.ans % (10 ** 9 + 7)

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target)] for _ in range(d)]
        for j in range(min(f, target)):
            dp[0][j] = 1
        for i in range(1, d):
            for j in range(i, target):
                dp[i][j] = sum(dp[i-1][max(0, j - f):j])
        return dp[-1][-1] % (10 ** 9 + 7)


if __name__ == '__main__':
    d = 1
    f = 6
    target = 3
    sol = Solution()
    print(sol.numRollsToTarget(d, f, target))
