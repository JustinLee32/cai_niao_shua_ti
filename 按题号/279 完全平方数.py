# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.


# method1
# dp
class Solution_dp:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while i-j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]


# BFS
from queue import Queue


class Solution2:
    def numSquares(self, n: int) -> int:
        around = []
        for i in range(1, n + 1):
            if i ** 2 <= n:
                around.append(i ** 2)
            else:
                break

        r = 0
        seen = set()  # 防止重复运算

        # ----------------BFS 开始----------------------
        # 初始化根节点
        q = Queue()
        q.put((0, r))

        # 进入队列循环
        while not q.empty():
            # 取出一个元素
            cur, step = q.get()
            step += 1

            # 放入周围元素
            for a in around:
                a += cur
                if a == n:
                    return step
                if a < n and (a, step) not in seen:
                    seen.add((a, step))
                    q.put((a, step))
        # ----------------------------------------------
        return 0


# myBFS


class Solution:
    def numSquares(self, n):
        element_list = []
        for i in range(1, n+1):
            if i ** 2 > n:
                break
            else:
                element_list.append(i ** 2)
        visted = set()
        queue = []
        queue.append((0, 0))
        while queue:
            temp = queue.pop(0)
            for element in element_list:
                if element > n - temp[0]:
                    break
                elif element == n - temp[0]:
                    return temp[1] + 1
                elif temp[0] + element in visted:
                    continue
                else:
                    visted.add(temp[0] + element)
                    queue.append((temp[0] + element, temp[1] + 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
