from operator import truediv


class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        def bsearch(arr, val):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == val:
                    return True
                elif arr[mid] < val:
                    low = mid + 1
                elif arr[mid] > val:
                    high = mid - 1
            return False

        arr2_sorted = sorted(arr2)
        count = 0

        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    count += 1

            

arr1, arr2, d = [4, 5, 8], [10, 9, 1, 8], 2
obj = Solution()
print(obj.findTheDistanceValue(arr1, arr2, d))