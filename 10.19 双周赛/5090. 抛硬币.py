from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[float(0) for _ in range(target + 1)] for _ in range(len(prob))]
        dp[0][0] = 1 - prob[0]
        for i in range(1, len(prob)):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i])
        if not target:
            return dp[-1][0]
        dp[0][1] = prob[0]
        for i in range(1, len(prob)):
            for j in range(1, min(len(dp[0]), i + 2)):
                dp[i][j] = dp[i-1][j] * (1 - prob[i]) + dp[i-1][j-1] * prob[i]
        return dp[-1][-1]


if __name__ == '__main__':
    prob = [0.5, 0.5, 0.5, 0.5, 0.5]
    target = 0
    sol = Solution()
    print(sol.probabilityOfHeads(prob, target))
