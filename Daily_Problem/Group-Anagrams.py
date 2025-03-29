class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            map_key = \\.join(sorted(list(s)))
            lst = mapping.get(map_key,[])
            lst.append(s)
            mapping[map_key]=lst
        return list(mapping.values())

        