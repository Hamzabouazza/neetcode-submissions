class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            for s in range(1, len(strs)):
                if i == len(strs[s]) or first[i] != strs[s][i]:
                    return prefix
            prefix += first[i]
        return prefix


            

            


        

        