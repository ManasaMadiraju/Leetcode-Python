class Solution:
    def romanToInt(self, s: str) -> int:
        romantoint={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)):
            if s[i] in romantoint: 
                res+=romantoint[s[i]]
        return res 
    # This code works for base case 

def main():
    s = "MCMXCIV"
    sol = Solution()
    result = sol.romanToInt(s)
    print(result)


if __name__ == "__main__":
    main()
