# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        dic = {}
        temp_list = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key, value in dic.items():
            temp_list.append((key, value))
        temp_list.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp_list[i][0])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
