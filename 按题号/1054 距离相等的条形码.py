from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) <= 2:
            return barcodes
        barcodes.sort()
        res = []
        half = len(barcodes) // 2
        flag = len(barcodes) % 2
        for i in range(half):
            res.append(barcodes[i])
            res.append(barcodes[half + i + flag])
        if flag:
            temp = barcodes[half]
            if temp != res[0]:
                res.insert(0, temp)
            else:
                res.append(temp)
        return res


if __name__ == '__main__':
    sol = Solution()
    barcodes = [2, 2, 1, 3]
    print(sol.rearrangeBarcodes(barcodes))
