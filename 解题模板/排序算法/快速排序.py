# -*- coding: utf-8 -*-


class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def partition(self, left, right):
        less = left - 1
        more = right + 1
        while left < more:
            if self.nums[left] < self.nums[right]:
                less += 1
                self.swap(less, left)
                left += 1
            elif self.nums[left] > self.nums[right]:
                more -= 1
                self.swap(more, left)
            else:
                left += 1
        return less + 1, more - 1

    def quick_sort(self, left, right):
        if left < right:
            p = self.partition(left, right)
            self.quick_sort(left, p[0] - 1)
            self.quick_sort(p[1] + 1, right)


if __name__ == '__main__':
    nums = [1, 10, 5, 3, 8, 7, 9]
    qc = QuickSort(nums)
    qc.quick_sort(0, len(nums) - 1)
    print(qc.nums)
