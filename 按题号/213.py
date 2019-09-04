class Solution:
	def rob(nums):
		if len(nums) == 0:
			return 0
		if len(nums) <= 2:
			return max(nums)
		#dp = [[0,0]] * len(nums) # 注意这种状态矩阵维度的定义; 第一个维度是钱，第二个维度是有没有抢第一间
		dp = [[0 for _ in range(2)] for _ in range(len(nums))]
		dp[0][0] = 0 # 不抢第一间
		dp[0][1] = nums[0] # 抢第一间
		dp[1][0] = nums[1]
		dp[1][1] = nums[0]
		for i in range(2,len(nums)):
			for j in range(2):
				dp[i][j] = max(dp[i-1][j],dp[i-2][j]+nums[i])
		dp[-1][0] = max(dp[-3][0]+nums[-1],dp[-2][0])
		dp[-1][1] = dp[-2][1]
		return max(dp[-1][0],dp[-1][1])

if __name__ == '__main__':
	print(Solution.rob([1,2,3,1]))