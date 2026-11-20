class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        melement = defaultdict(int)
        res, maxCount = 0, 0

        for num in nums:
            melement[num] += 1

            if maxCount < melement[num]:
                res = num
                maxCount = melement[num]
        return res


        





             
        

        
        