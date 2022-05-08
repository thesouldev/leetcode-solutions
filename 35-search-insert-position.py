class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1

        if nums:
            while low <= high:
                mid = (low+high)//2

                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                if nums[mid] > target:
                    high = mid - 1

            if nums[mid] < target:
                return mid + 1
            else:
                return mid


list = [-3, -1, 5, 6]
target = 0
obj = Solution()
print(obj.searchInsert(list, target))
