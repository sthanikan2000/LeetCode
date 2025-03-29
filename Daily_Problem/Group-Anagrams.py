from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ######################## DEFAULT DICTIONARY ########################################
        >>> s = defaultdict()
        >>> s
            defaultdict(None, {})
        ------------------------------------------------------------------------------------
        -> A sub-class of the dictionary class that returns a dictionary-like object.
        ------------------------------------------------------------------------------------
        >>> s = defaultdict(int)
        >>> s
            defaultdict(<class 'int'>, {})
        >>> s[2]
            0
        '''

        '''
        ### Time Complexity: O(n*m)
        str_map = defaultdict(list)
        for s in strs:
            map_key = [0]*26
            for c in s:
                map_key[ord(c)-ord(\a\)] +=1
            str_map[tuple(map_key)].append(s)
        return list(str_map.values())
        '''
        
        ### Time Complexity O(n*m*log(m))
        mapping = defaultdict(list)
        for s in strs: ### n iterations
            map_key = tuple(sorted(s)) ### O(m*log(m)) ; 0<=m<=100
            mapping[map_key].append(s)
        return list(mapping.values())

        