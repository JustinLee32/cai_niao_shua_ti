#给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#示例 1:
#
#输入: coins = [1, 2, 5], amount = 11
#输出: 3 
#解释: 11 = 5 + 5 + 1
#示例 2:
#
#输入: coins = [2], amount = 3
#输出: -1
#说明:
#你可以认为每种硬币的数量是无限的。
#

# dp[n] = 1 + min(dp[n-coins[i]] for i in range(len(coins))

class Solution:
	def coinChange(self, coins, amount: int) -> int:
		dp = [float("inf") for _ in range(amount + 1)]
		dp[0] = 0
		for i in range(amount + 1):
			for j in range(len(coins)):
				if i - coins[j] >= 0:
					dp[i] = min(dp[i - coins[j]] + 1, dp[i])
		return dp[-1] if dp[-1] != float("inf") else -1
		

if __name__ == "__main__":
	print(Solution.coinChange(None, [370,417,408,156,143,434,168,83,177,280,117]
	, 9953))