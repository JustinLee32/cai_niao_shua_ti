from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        cache = (coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1])
        for i in range(2, len(coordinates)):
            if (coordinates[i][1] - coordinates[0][1]) * cache[0] != (coordinates[i][0] - coordinates[0][0]) * cache[1]:
                return False
        return True


if __name__ == '__main__':
    coordinates = [[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]
    sol = Solution()
    print(sol.checkStraightLine(coordinates))
