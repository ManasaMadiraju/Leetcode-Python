class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')':'(','}':'{',']':'['}

        for c in s:
            if c not in hashMap:
                stack.append(c)
            else:
                if stack and hashMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack