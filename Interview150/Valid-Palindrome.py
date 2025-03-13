ALPHA_NUMERIC_RANGE=list(range(48,58))+list(range(65,91))+list(range(97,123))
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        sta=0
        end=len(s)-1
        while sta<end:
            ord_sta=ord(s[sta])
            ord_end=ord(s[end])
            if ord_sta not in ALPHA_NUMERIC_RANGE:
                sta+=1
                continue
            if ord_end not in ALPHA_NUMERIC_RANGE:
                end-=1
                continue
            if s[sta].lower() != s[end].lower():
                # print(sta,s[sta],end,s[end])
                return False
            # print(sta,end)
            sta+=1
            end-=1
        return True

        