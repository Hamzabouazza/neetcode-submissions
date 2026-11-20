class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        if not strs:
            return ""
        groups = {}

        for s in strs:
            label = "".join(sorted(s))

            if label not in groups:
                groups[label] = []

            groups[label].append(s)
        return list(groups.values())


        