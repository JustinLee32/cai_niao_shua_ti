from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = (arr[-1] - arr[0]) / len(arr)
        temp = arr[0]
        flag = 0
        for i in range(1, len(arr)):
            if arr[i] - temp != difference:
                flag = i
                break
            else:
                temp = arr[i]
                continue
        return int(arr[flag] - difference)


if __name__ == '__main__':
    arr = [5, 7, 11, 13]
    sol = Solution()
    print(sol.missingNumber(arr))
