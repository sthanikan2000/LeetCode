class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            x = mag.get(c,0)
            mag[c] = x+1
        for c in ransomNote:
            x = mag.get(c,0)
            if x==0:
                return False
            mag[c] = x-1
        return True
        