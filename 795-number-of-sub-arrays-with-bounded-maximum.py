class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        ans = count = 0
        prev = -1

        for index, num in enumerate(nums):
            if left <= num <= right:
                count = index - prev
            elif num > right:
                prev = index
                count = 0

            ans += count

        return ans


nums, left, right = [2,1,4,3], 2, 3
obj = Solution()
print(obj.numSubarrayBoundedMax(nums, left, right))
