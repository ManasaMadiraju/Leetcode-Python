class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result=result+s[i]
            else:
                continue
        result=result.lower()
        rev=result[::-1]
        if(rev == result):
            return True
        else:
            return False
            

def main():
    sln=Solution()
    x=" "
    print(sln.isPalindrome(x))


if __name__ == "__main__":
    main()

