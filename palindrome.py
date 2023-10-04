class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x).lower()
        y=x[::-1]
        if (x==y):
            return True
        else:
            return False
        

def main():
    x=141
    s=Solution()
    print(s.isPalindrome(x))

if __name__ == "__main__":
    main()