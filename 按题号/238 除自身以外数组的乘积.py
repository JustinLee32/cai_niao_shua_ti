class Solution:
    def productExceptSelf(self, nums: list) -> list:
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
