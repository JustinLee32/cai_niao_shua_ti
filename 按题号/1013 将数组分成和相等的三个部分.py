# -*- coding: utf-8 -*-
# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。 
#
# 示例 1：
#
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 示例 2：
#
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 示例 3：
#
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
# 提示：
#
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000


from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        each_part = sum(A) / 3
        if each_part % 1:
            return False
        else:
            [left, right] = [-1, -1]
            temp = 0
            for i in range(len(A)):
                temp += A[i]
                if temp == each_part:
                    left = i
                    temp = 0
                    break
                else:
                    continue
            if left < 0:
                return False
            for i in range(left+1, len(A)):
                temp += A[i]
                if temp == each_part:
                    right = i
                    break
                else:
                    continue
            return True if 1 <= right < len(A) - 1 else False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canThreePartsEqualSum([12,-4,16,-5,9,-3,3,8,0]))
