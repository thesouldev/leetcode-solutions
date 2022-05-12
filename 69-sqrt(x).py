class Solution:
    def mySqrt(self, x: int) -> int:
        val = x
        offset = 1
        count = 0
        while(val) > 0:
            val = val - offset
            offset += 2
            count += 1
        if val == 0:
            return count
        else:
            return count - 1


val = 5
obj = Solution()
print(obj.mySqrt(val))
