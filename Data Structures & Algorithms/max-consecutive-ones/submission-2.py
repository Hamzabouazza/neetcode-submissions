class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res= 0
        maxRes = 0
        for num in nums: 
            if num == 1:
                res+=1
                maxRes = max(res, maxRes)
            else:
                res = 0
        return maxRes
        