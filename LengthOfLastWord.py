class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip(" ")
        s=s.split(" ")
        return len(s[-1])


def main():
    sln=Solution()
    s= "   fly me   to   the moon  "
    print(sln.lengthOfLastWord(s))

if __name__ == "__main__":
    main()


