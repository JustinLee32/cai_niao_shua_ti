#给定一个含有 n 个  !!正整数的数组!!  和一个正整数 s ，找出该数组中满足其和 ≥ s 的  !!长度最小的连续子数组!!  。如果不存在符合条件的连续子数组，返回 0。
#
#示例: 
#
#输入: s = 7, nums = [2,3,1,2,4,3]
#输出: 2
#解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#进阶:
#
#如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

s = 7; nums = [2,3,1,2,4,3]
if len(nums)<=1:
	if sum(nums)>=s:
		print(len(nums))
	else:
		print(0)
left = 0; res = float('inf'); add = 0
for right in range(len(nums)):
	add += nums[right]
	while add >= s:
		res = min(res, right - left + 1)
		add -= nums[left]
		left += 1
if res == float('inf'):
	print(0)
print(res)