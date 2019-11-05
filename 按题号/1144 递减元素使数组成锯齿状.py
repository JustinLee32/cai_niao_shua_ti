# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。


from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res_odd_bigger = 0
        res_even_bigger = 0
        if len(nums) <= 2:
            return 0
        # 奇数大
        probe = 1
        temp = nums[probe - 1]
        while probe < len(nums):
            if probe % 2:
                if nums[probe] >= temp:
                    res_odd_bigger += nums[probe] - temp + 1
                    temp -= 1
                else:
                    temp = nums[probe]
            elif not probe % 2:
                if nums[probe] <= temp:
                    res_odd_bigger += temp - nums[probe] + 1
                    temp = nums[probe]
                else:
                    temp = nums[probe]
            probe += 1
        # 偶数大
        probe = 1
        temp = nums[probe - 1]
        while probe < len(nums):
            if not probe % 2:
                if nums[probe] >= temp:
                    res_even_bigger += nums[probe] - temp + 1
                    temp -= 1
                else:
                    temp = nums[probe]
            elif probe % 2:
                if nums[probe] <= temp:
                    res_even_bigger += temp - nums[probe] + 1
                    temp = nums[probe]
                else:
                    temp = nums[probe]
            probe += 1
        return min(res_odd_bigger, res_even_bigger)


if __name__ == '__main__':
    nums = [9, 6, 1, 6, 2]
    sol = Solution()
    print(sol.movesToMakeZigzag(nums))
