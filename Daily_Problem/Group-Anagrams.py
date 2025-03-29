class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ### Time Complexity: O(n*m)
        c_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        str_map = {}
        for s in strs:
            map_key = [0]*26
            for c in s:
                map_key[c_map[c]] +=1
            map_key = tuple(map_key)
            lst = str_map.get(map_key,[])
            lst.append(s)
            str_map[map_key] = lst
        return list(str_map.values())
        '''
        
        ### Time Complexity O(n*m*log(m))
        mapping = {}
        for s in strs: ### n iterations
            map_key = tuple(sorted(s)) ### O(m*log(m)) ; 0<=m<=100
            lst = mapping.get(map_key,[])
            lst.append(s)
            mapping[map_key]=lst
        return list(mapping.values())
        

        