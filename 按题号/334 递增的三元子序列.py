# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 3:
            return False

        min_num = float('inf')
        max_num = float('inf')

        for n in nums:
            if n < min_num:
                min_num = n
            elif min_num < n <= max_num:
                # 如果下一个值大于最小值，且小于中间值，则我们使用该值作为中间值(因为如果最小的中间值都得不到解，那么就是false，这样也保证了覆盖所有的情况)。
                max_num = n
            elif n > max_num:
                return True

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.increasingTriplet())
