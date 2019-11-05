# 给出三个均为
# 绝对升序排列
# 的整数数组
# arr1，arr2
# 和
# arr3。
#
# 返回由
# 仅
# 在这三个数组中
# 同时出现
# 的整数构成一个有序数组。
#
#
#
# 示例：
#
# 输入: arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 5, 7, 9], arr3 = [1, 3, 4, 5, 8]
# 输出: [1, 5]
# 解释: 只有
# 1
# 和
# 5
# 同时在这三个数组中出现.
#
# 提示：
#
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000


from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    sol = Solution()
    print(sol.arraysIntersection(arr1, arr2, arr3))