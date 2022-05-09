class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = num
        offset = 1
        while(val > 0):
            val = val - offset
            offset = offset + 2
        if val == 0:
            return True
        else:
            return False


num = 9
obj = Solution()
print(obj.isPerfectSquare(num))
