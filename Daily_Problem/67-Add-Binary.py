class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=""
        extra=0
        while a and b:
            temp_add=int(a[-1])+int(b[-1])+extra
            if temp_add<=1:
                extra=0
                c= str(temp_add) + c
            elif temp_add==2:
                extra=1
                c="0"+c
            else:
                extra=1
                c="1"+c
            a=a[:-1]
            b=b[:-1]
            print(a,b)
        remaining = a if a else b
        while extra:
            if remaining:
                temp_add=int(remaining[-1])+extra
                if temp_add==2:
                    extra=1
                    c="0"+c
                else:
                    extra=0
                    c="1"+c
                remaining = remaining[:-1]
            else:
                c="1"+c
                extra=0
        if remaining:
            c=remaining+c
        return c
            

        