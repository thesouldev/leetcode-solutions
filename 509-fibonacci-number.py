"""
Complexity Analysis:
Time - O(n)
Space - O(1)

"""

class Solution:
    def fib(self, n: int) -> int:
        def fibo(n):
            if n < 2:
                return n
            return fibo(n-2) + fibo(n-1)
        
        return fibo(n)

