class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Time Complexity O(n*m*log(m))
        mapping = {}
        for s in strs: ### n iterations
            map_key = tuple(sorted(list(s))) ### O(m*log(m)) ; 0<=m<=100
            lst = mapping.get(map_key,[])
            lst.append(s)
            mapping[map_key]=lst
        return list(mapping.values())

        