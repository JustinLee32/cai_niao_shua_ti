# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10_7 周赛.5 双周赛, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。

import heapq


class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        if k == 0:
            return None
        if k == 1:
            return matrix[0][0]
        temp_list = []
        for i in range(k // len(matrix)):
            temp_list += matrix[i]
        if k % len(matrix):
            temp_list += matrix[k // len(matrix)][:k % len(matrix)]
        temp_list.sort()
        row = k // len(matrix)
        column = k % len(matrix)
        for i in range(row, len(matrix)):
            if i == row:
                for j in range(column, len(matrix)):
                    if matrix[i][j] >= temp_list[-1]:
                        break
                    else:
                        temp_list.pop()
                        temp_list.append(matrix[i][j])
                        temp_list.sort()
            else:
                for j in range(len(matrix)):
                    if matrix[i][j] >= temp_list[-1]:
                        break
                    else:
                        temp_list.pop()
                        temp_list.append(matrix[i][j])
                        temp_list.sort()
        return temp_list[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.kthSmallest([[1, 2],
                           [1, 3]], 4))
