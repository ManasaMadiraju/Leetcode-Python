class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    for i, d in reversed(list(enumerate(digits))):
      if d < 9:
        digits[i] += 1
        return digits
      digits[i] = 0

    return [1] + digits



        



def main():
    sln=Solution()
    digits=[1,2,3]
    print(sln.plusOne(digits))

if __name__ == "__main__":
    main()
