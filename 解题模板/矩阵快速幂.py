from typing import List


class MatrixMultiply:
    def __init__(self):
        pass

    def matrix_multiply(self, matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
        matrix_c = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
        for i in range(len(matrix_c)):
            for j in range(len(matrix_c[0])):
                for k in range(len(matrix_b)):
                    matrix_c[i][j] += matrix_a[i][k] + matrix_b[k][j]
        return matrix_c


class EyesMatrix:
    def __init__(self):
        pass

    def generate_eyes_matrix(self, size: int) -> List[List[float]]:
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            matrix[i][i] = 1
        return matrix


class FastExponentiationOfMatrix(MatrixMultiply, EyesMatrix):
    def __init__(self, matrix: List[List[float]], power: int):
        # 做矩阵快速幂运算要求为方阵
        self.matrix = matrix
        self.power = power
        super(MatrixMultiply).__init__()
        super(MatrixMultiply).__init__()

    def matrix_fast_exponentiation(self):
        def _recursion(matrix: List[List[float]], power: int) -> List[List[float]]:
            if not power:
                return self.generate_eyes_matrix(len(self.matrix))
            # if power < 0:
            # 求逆矩阵，还没想好咋写- -

            if power == 1:
                return matrix
            temp = _recursion(matrix, power // 2)
            if power & 1:
                return self.matrix_multiply(matrix, self.matrix_multiply(temp, temp))
            else:
                return self.matrix_multiply(temp, temp)

        return _recursion(self.matrix, self.power)


if __name__ == '__main__':
    matrix = [[0, 1, 0, 0, 0],
              [1, 0, 1, 0, 0],
              [1, 1, 0, 1, 1],
              [0, 0, 1, 0, 1],
              [1, 0, 0, 0, 0]]
    power = 50
    feom = FastExponentiationOfMatrix(matrix, power)
    print(feom.matrix_fast_exponentiation())
