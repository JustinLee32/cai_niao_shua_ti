from typing import List


class Solution:
    def _insert(self, cache: List[List[int]], new: List[int]) -> List[List[int]]:
        if not cache:
            cache.append(new)
            return cache
        elif cache:
            for i in range(len(cache) - 1, -1, -1):
                if new[2] >= cache[i][2]:
                    cache.insert(i+1, new)
                    return cache
                else:
                    continue
            cache.insert(0, new)
            return cache

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cache = []
        passengers = 0
        trips.sort(key=lambda x: (x[1], x[2]))
        for trip in trips:
            # 下车
            while cache and cache[0][2] <= trip[1]:
                passengers -= cache.pop(0)[0]
            # 上车
            if passengers + trip[0] <= capacity:
                passengers += trip[0]
                cache = self._insert(cache, trip)
                continue
            elif passengers + trip[0] > capacity:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11
    print(sol.carPooling(trips, capacity))
