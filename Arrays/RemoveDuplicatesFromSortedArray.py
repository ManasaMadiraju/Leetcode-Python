class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
    
def main():
        nums=[0,0,1,1,1,2,2,3,3,4]
        s=Solution()
        result=s.removeDuplicates(nums)
        print(result)


if __name__ == "__main__":
    main()

        
