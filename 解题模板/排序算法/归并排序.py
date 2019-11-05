# -*- coding: utf-8 -*-


class MergeSort:
    def __init__(self, nums):
        self.nums = nums

    def merge_sort(self, left, right):
        if left == right:
            return
        mid = (left + right) >> 1
        self.merge_sort(left, mid)
        self.merge_sort(mid + 1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        helper = [0 for _ in range(right - left + 1)]
        pointer1, pointer2, pointer3 = left, mid + 1, 0
        while pointer1 <= mid and pointer2 <= right:
            if self.nums[pointer1] < self.nums[pointer2]:
                helper[pointer3] = self.nums[pointer1]
                pointer1 += 1
            else:
                helper[pointer3] = self.nums[pointer2]
                pointer2 += 1
            pointer3 += 1
        while pointer1 <= mid:
            helper[pointer3] = self.nums[pointer1]
            pointer1 += 1
            pointer3 += 1
        while pointer2 <= right:
            helper[pointer3] = self.nums[pointer2]
            pointer2 += 1
            pointer3 += 1
        for i in range(len(helper)):
            self.nums[left+i] = helper[i]


if __name__ == '__main__':
    nums = [1, 10, 5, 3, 8, 7, 9]
    ms = MergeSort(nums)
    ms.merge_sort(0, len(nums) - 1)
    print(ms.nums)
