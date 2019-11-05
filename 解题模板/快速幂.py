class FastExponentiation:
    def __init__(self, num: float, power: int):
        self.num = num
        self.power = power

    def fast_exponentiation(self):
        def _recursion(num: float, power: int) -> float:
            if not power:
                return 1
            if power < 0:
                return _recursion(1 / num, -power)
            if power == 1:
                return num
            if power & 1:
                return num * _recursion(num, power // 2) ** 2
            else:
                return _recursion(num, power // 2) ** 2

        return _recursion(self.num, self.power)


if __name__ == '__main__':
    fe = FastExponentiation(num=2, power=2000000)
    print(fe.fast_exponentiation())
