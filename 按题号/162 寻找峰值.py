# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。


class Solution:
    def findPeakElement(self, nums: list) -> int:
        if len(nums) <= 2:
            return nums.index(max(nums))
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        flag = 0
        while left < mid < right:
            if nums[left] <= nums[mid] and nums[right] <= nums[mid]:
                left = int((left + mid) / 2)
                right = int((right + mid + 1) / 2)
                flag = 1
            elif nums[left] > nums[mid]:
                right = mid
                mid = int((left + mid) / 2)
                flag = 0
            elif nums[right] > nums[mid]:
                left = mid
                mid = int((mid + right) / 2)
                flag = 2
            if max(right - mid, mid - left) <= 1:
                return max([(nums[left], left), (nums[mid], mid), (nums[right], right)], key=lambda x: x[0])[1]
        if flag == 0:
            return left
        elif flag == 1:
            return mid
        else:
            return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1,2,1,3,5,6,4]))
