class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #print (len(nums))
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    #print("Match Found at "+str(i)+","+str(j))
                    #print(i,j)
                    result.append(i)
                    result.append(j)
                    print(result)



def main():
    sln = Solution()
    nums=[2,7,11,15]
    print(nums)
    target=int(input("Enter Target: "))
    sln.twoSum(nums, target)

if __name__ == "__main__":
    main()

