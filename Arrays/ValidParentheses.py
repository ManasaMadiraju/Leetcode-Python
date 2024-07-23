class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ClosetoOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in ClosetoOpen:
                if stack and stack[-1] == ClosetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


def main():
    s = "()[]{}"
    sol=Solution()
    result = sol.isValid(s)
    print(result)


if __name__ == "__main__":
    main()