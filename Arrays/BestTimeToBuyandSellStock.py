class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        l, r = 0, 1
        maxP = 0 
        while r < len(nums):
            if nums[l] < nums[r]:
                profit = nums[r]-nums[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        
        return maxP


def main():
    nums=[1,2,3,1,1,3]
    s=Solution()
    result=s.maxProfit(nums)
    print(result)


if __name__ == "__main__":
    main() 