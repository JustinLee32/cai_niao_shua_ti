from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: (x[0], x[1]))
        slots2.sort(key=lambda x: (x[0], x[1]))
        first, second = 0, 0
        while first < len(slots1) and second < len(slots2):
            temp1 = slots1[first]
            temp2 = slots2[second]
            if self.check_time(temp1, temp2, duration):
                cache = max(temp1[0], temp2[0])
                return [cache, cache + duration]
            else:
                if temp2[1] > temp1[1]:
                    first += 1
                else:
                    second += 1
        return []

    def check_time(self, temp1: List[int], temp2: List[int], duration: int) -> bool:
        start = max(temp1[0], temp2[0])
        end = min(temp1[1], temp2[1])
        return True if end - start >= duration else False


if __name__ == '__main__':
    slots1 = [[216397070, 363167701], [98730764, 158208909], [441003187, 466254040], [558239978, 678368334], [683942980, 717766451]]
    slots2 = [[50490609, 222653186], [512711631, 670791418], [730229023, 802410205], [812553104,891266775], [230032010, 399152578]]
    duration = 456085
    sol = Solution()
    print(sol.minAvailableDuration(slots1, slots2, duration))
