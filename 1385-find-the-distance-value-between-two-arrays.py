"""
Method: 1385. Find the Distance Value Between Two Arrays
Time Complexity: O(n2)
Space Complexity: O(1)
"""
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        count = 0
        for i in arr1:
            count += 1
            for j in arr2:
                if abs(i-j) <= d:
                    count -= 1
                    break
                
        return count

            

arr1, arr2, d = [2,1,100,3], [-5,-2,10,-3,7], 6
obj = Solution()
print(obj.findTheDistanceValue(arr1, arr2, d))