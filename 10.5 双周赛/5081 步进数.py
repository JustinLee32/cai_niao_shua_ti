# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是
# 1，那么这个数就是一个「步进数」。
#
# 例如，321
# 是一个步进数，而
# 421
# 不是。
#
# 给你两个整数，low
# 和
# high，请你找出在[low, high]
# 范围内的所有步进数，并返回
# 排序后
# 的结果。
#
#
#
# 示例：
#
# 输入：low = 0, high = 21
# 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10_7 周赛, 12, 21]
#
# 提示：
#
# 0 <= low <= high <= 2 * 10_7 周赛 ^ 9

from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        if high <= 10:
            return list(range(low, high + 1))
        self.ans = []
        if low <= 10:
            self.ans += list(range(low, 10))

        def _recursive(low, high, num: int) -> None:
            num_string = str(num)
            if num_string[-1] == '0':
                if low <= int(num_string + '1') <= high:
                    self.ans.append(int(num_string + '1'))
                    _recursive(low, high, int(num_string + '1'))
                elif int(num_string + '1') < low:
                    _recursive(low, high, int(num_string + '1'))
                elif int(num_string + '1') > high:
                    return
            elif num_string[-1] == '9':
                if low <= int(num_string + '8') <= high:
                    self.ans.append(int(num_string + '8'))
                    _recursive(low, high, int(num_string + '8'))
                elif int(num_string + '8') < low:
                    _recursive(low, high, int(num_string + '8'))
                elif int(num_string + '8') > high:
                    return
            else:
                small_string = str(int(num_string[-1]) - 1)
                big_string = str(int(num_string[-1]) + 1)
                subtract_one = int(num_string + small_string)
                add_one = int(num_string + big_string)
                if low <= add_one <= high:
                    self.ans.append(add_one)
                    _recursive(low, high, add_one)
                if low <= subtract_one <= high:
                    self.ans.append(subtract_one)
                    _recursive(low, high, subtract_one)
                if subtract_one < low:
                    _recursive(low, high, subtract_one)
                if add_one < low:
                    _recursive(low, high, add_one)
                if subtract_one > high:
                    return

        for i in range(1, 10):
            _recursive(low, high, i)
        return sorted(self.ans)


if __name__ == '__main__':
    low = 0
    high = 15
    sol = Solution()
    print(sol.countSteppingNumbers(low, high))
