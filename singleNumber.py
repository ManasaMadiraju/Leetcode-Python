class Solution:
    def singleNumber(self, nums: list[int]) -> int: 
       result_dist = {}
       for index in range(len(nums)):
           if (nums[index] in result_dist):
               result_dist[nums[index]] = result_dist[nums[index]] +1
           else:
               result_dist[nums[index]] = 1
        
       for keys in result_dist:
           if(result_dist[keys] == 1):
               return keys

                
def main():
    s=Solution()
    nums=[4,1,2,1,2]
    print(s.singleNumber(nums))


if __name__ == "__main__":
    main()