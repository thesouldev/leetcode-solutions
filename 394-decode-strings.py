"""
Complexity Analysis:
Time - O(n)
Space - O(n)
"""

class Solution(object):
    def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            # base condition
            if s[i] != ']':
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()

                k=""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substring)
        return "".join(stack)


string="3[a]2[bc]"
result=Solution().decodeString(string)
print(result)