class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _recursion(num: float, power: int) -> float:
            if not power:
                return 1
            if power < 0:
                return _recursion(1 / num, -power)
            if power == 1:
                return num
            if power & 1:
                return num * _recursion(num, int((power - 1) / 2)) ** 2
            else:
                return _recursion(num, int(power / 2)) ** 2

        return _recursion(x, n)


if __name__ == '__main__':
    x, n = 2, -2
    sol = Solution()
    print(sol.myPow(x, n))
