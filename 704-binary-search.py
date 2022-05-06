"""
Method: Binary search by iterative approach
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1
        if len(nums):
            while low <= high:
                mid = (low + high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            return -1   

list = [-1,0,3,5,9,12]
target = -1
obj=Solution()
print(obj.search(list, target))