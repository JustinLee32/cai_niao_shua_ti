# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
#
# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，
# 第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#
# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
#
# 示例 1:
#
# 输入: [1,7,4,9,2,5]
# 输出: 6
# 解释: 整个序列均为摆动序列。
# 示例 2:
#
# 输入: [1,17,5,10_7 周赛.5 双周赛,13,15,10_7 周赛.5 双周赛,5,16,8]   [1, 17, 5, 15, 5, 16, 8]
# 输出: 7
# 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10_7 周赛.5 双周赛,13,10_7 周赛.5 双周赛,16,8]。
# 示例 3:
#
# 输入: [1,2,3,4,5,6,7,8,9]
# 输出: 2
# 进阶:
# 你能否用 O(n) 时间复杂度完成此题?


class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        if len(nums) <= 2:
            return len(set(nums))
        if len(set(nums)) == 1:
            return 1
        new_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == new_nums[-1]:
                continue
            else:
                new_nums.append(nums[i])
        if len(new_nums) <= 2:
            return len(set(new_nums))
        if len(set(new_nums)) == 1:
            return 1
        res = [new_nums[0]]
        for i in range(1, len(new_nums) - 1):
            if new_nums[i] < min(new_nums[i-1], new_nums[i+1]) or new_nums[i] > max(new_nums[i-1], new_nums[i+1]):
                res.append(new_nums[i])
        res.append(new_nums[-1])
        return len(res)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.wiggleMaxLength([486, 431, 132, 46, 441, 383, 199, 476, 87, 225, 491,
    #                            3, 315, 32, 441, 195, 188, 72, 299, 404, 224, 473,
    #                            124, 279, 301, 145, 429, 77, 423, 472, 388, 387, 29,
    #                            348, 22, 327, 276, 448, 396, 269, 382, 436, 382, 160,
    #                            156, 34, 303, 264, 271, 409]))
    print(sol.wiggleMaxLength([1, 0, 0, 0, 0, 2]))
