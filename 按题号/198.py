nums = [2,7,9,3,1]
if len(nums)<=1:
	print(sum(nums))
dp = [0]*len(nums)
dp[0] = nums[0]
for i in range(1,len(nums)):
	dp[i] = max(dp[i-1],dp[i-2]+nums[i])
print(dp[len(nums)-1])