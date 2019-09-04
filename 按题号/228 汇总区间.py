#给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
#示例 1:
#
#输入: [0,1,2,4,5,7]
#输出: ["0->2","4->5","7"]
#解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#示例 2:
#
#输入: [0,2,3,4,6,8,9]
#输出: ["0","2->4","6","8->9"]
#解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#

class Solution:
	def summaryRanges(self, nums):
		if len(nums) == 0:
			return []
		if len(nums) == 1:
			return [str(nums[0])]
		res = [str(nums[0])]; flag = 0
		def iscontinue(i,nums):
			if nums[i] == nums[i-1] + 1:
				return True
			else:
				return False
		for i in range(1,len(nums)):
			if iscontinue(i, nums):
				flag = 1
			else:
				if flag == 1:
					res[-1] += ("->" + str(nums[i-1]))
					res.append(str(nums[i]))
					flag = 0
				else:
					res.append(str(nums[i]))
		if flag == 1:
			res[-1] += ("->" + str(nums[i]))
		return res
if __name__ == "__main__":
	print(Solution.summaryRanges(None, [0,2,3,4,6,8,9]))