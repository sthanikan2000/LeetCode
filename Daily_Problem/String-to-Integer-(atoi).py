class Solution:
    def myAtoi(self, s: str) -> int:
        map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        res = 0
        neg = None
        firstValidCharacterRead = False
        for c in s:
            if c in map:
                if not firstValidCharacterRead:
                    firstValidCharacterRead = True
                res = res*10 + map[c]
            elif not firstValidCharacterRead:
                if c==\ \:
                    continue
                elif c==\-\ and neg == None:
                    neg = True
                    firstValidCharacterRead = True
                elif c == \+\ and neg == None:
                    neg = False
                    firstValidCharacterRead = True
                else:
                    break
            else:
                break
        lower_bound = -(1 << 31)
        upper_bound = (1 << 31) - 1
        if neg:
            res = 0 - res
        if res < lower_bound:
            return lower_bound
        if res > upper_bound:
            return upper_bound
        return res



        '''
        ### Valid solution, but usage of int()
        res = \\
        for i in s:
            if i == \ \ and not res:
                continue
            elif i in [\+\,\-\] and not res:
                res += i
            elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                res += i
            else:
                break
        if res in [\\,\+\,\-\]:
            return 0
        y = int(res)
        if y > 2147483647:
            return 2147483647
        elif y < -2147483648:
            return -2147483648
        else:
            return y'''                
            

        