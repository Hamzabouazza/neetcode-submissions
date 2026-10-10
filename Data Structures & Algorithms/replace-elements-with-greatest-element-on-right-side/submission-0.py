class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        res = [0] * n
        for i in range(n):
            current_max = -1
            for j in range(i+1, n):
                current_max = max(arr[j], current_max)
            res[i] = current_max
        return res

        