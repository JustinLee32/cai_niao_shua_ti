# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
#
# 找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 示例 3:
#
# 输入: nums1 = [1,2], nums2 = [3], k = 3
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#


# class Solution:
#     def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
#         res = []
#         if not k:
#             return res
#         res.append([nums1[0], nums2[0]])
#         if k == 1:
#             return res
#         size1 = len(nums1)
#         size2 = len(nums2)
#         row, column = 0, 0
#         for i in range(1, k):
#             if row == 0:
#                 if column < size2 - 1:
#                     temp = min([(nums1[row + 1] + nums2[column], 1), (nums1[row] + nums2[column + 1], 2)],
#                                key=lambda x: x[0])
#                     if temp[1] == 1:
#                         row += 1
#                         res.append([nums1[row], nums2[column]])
#                     elif temp[1] == 2:
#                         column += 1
#                         res.append([nums1[row], nums2[column]])
#                 else:
#                     row += 1
#                     res.append([nums1[row], nums2[column]])
#             elif row == size1 - 1:
#                 if column == size2 - 1:
#                     return res
#                 temp = min([(nums1[row - 1] + nums2[column + 1], 1), (nums1[row] + nums2[column + 1], 2)],
#                            key=lambda x: x[0])
#                 if temp[1] == 1:
#                     row -= 1
#                     column += 1
#                     res.append([nums1[row], nums2[column]])
#                 elif temp[1] == 2:
#                     column += 1
#                     res.append([nums1[row], nums2[column]])
#             elif column == size2 - 1:
#                 if row == size1 - 1:
#                     return res
#                 row += 1
#                 res.append([nums1[row], nums2[column]])
#             else:
#                 temp = min([(nums1[row + 1] + nums2[column], 1), (nums1[row] + nums2[column + 1], 2),
#                             (nums1[row - 1] + nums2[column + 1], 3), (nums1[row + 1] + nums2[column - 1], 4)],
#                            key=lambda x: x[0])
#                 if temp[1] == 1:
#                     row += 1
#                     res.append([nums1[row], nums2[column]])
#                 elif temp[1] == 2:
#                     column += 1
#                     res.append([nums1[row], nums2[column]])
#                 elif temp[1] == 3:
#                     column += 1
#                     row -= 1
#                     res.append([nums1[row], nums2[column]])
#                 elif temp[1] == 4:
#                     row += 1
#                     column -= 1
#                     res.append([nums1[row], nums2[column]])
#         return res


class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        res = []
        temp_list = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                temp_list.append([nums1[i], nums2[j]])
        temp_list.sort(key=lambda x: sum(x))
        return temp_list[:k] if k <= len(temp_list) else temp_list


# 利用堆排序
import heapq
class Solution:
    def kSmallestPairs2(self, nums1: list, nums2: list, k: int) -> list:
        res = []
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return res
        heap = [[nums1[0]+nums2[i], 0, i] for i in range(len(nums2))]
        # 利用堆每次取最小的
        while k and heap:
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1:
                heapq.heappush(heap, [nums1[i+1] + nums2[j], i+1, j])
            k -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
