class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        for i in range(n):
            maxRight = -1
            for j in range(i + 1, n):
                maxRight = max(maxRight, arr[j])
            res[i] = maxRight
        return res

        



        