# 324.摆动排序II
#给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
#示例 1:
#
#输入: nums = [1, 5, 1, 1, 6, 4]
#输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
#示例 2:
#
#输入: nums = [1, 3, 2, 2, 3, 1]
#输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
#说明:
#你可以假设所有输入都会得到有效的结果。
#
#进阶:
#你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

class Solution:
	def wiggleSort(self, nums) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		nums_copy = nums.copy()
		nums_copy.sort()
		nums_1 = nums_copy[:(len(nums)+1)//2]; nums_2 = nums_copy[(len(nums)+1)//2:]
		for i in range(len(nums)//2):
			nums[2*i] = nums_1[i]
			nums[2*i+1] = nums_2[i]
		if len(nums) % 2:
			nums[-1] = nums_copy[len(nums)//2]
		return nums
		
if __name__ == "__main__":
	print(Solution.wiggleSort(None, [4,5,5,6]))