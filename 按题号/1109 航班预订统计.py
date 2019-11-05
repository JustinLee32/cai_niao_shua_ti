# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
# 请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。


from typing import List


# 前缀和解法
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for start, end, val in bookings:
            ans[start - 1] += val
            if end < n: ans[end] -= val
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    sol = Solution()
    print(sol.corpFlightBookings(bookings, n))
