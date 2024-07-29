class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range (2):
            for n in nums:
                ans.append(n)
        return ans
    
    
def main():
    nums = [1,2,3]
    s = Solution()
    result = s.getConcatenation(nums)
    print(result)


if __name__ == "__main__":
    main()