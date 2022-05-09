class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        if not A:
            return -1

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[end] > A[start]:
            return end
        else:
            return start

        return -1


list = [3, 4, 5, 1]
obj = Solution()
print(obj.peakIndexInMountainArray(list))
