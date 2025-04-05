class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = ""
        i = 0
        dolar_sta_ind  = None
        n = len(sentence)
        while i < n:
            if dolar_sta_ind == None and sentence[i] == "$" and (i==0 or sentence[i-1]==" "):
                res += sentence[i]
                dolar_sta_ind = i+1
            elif dolar_sta_ind == None:
                res += sentence[i]
            elif dolar_sta_ind != None and sentence[i] == " ":
                price = sentence[dolar_sta_ind:i]
                dolar_sta_ind = None
                if not price.isnumeric():
                    res += price + " "
                else:
                    res += f"%.2f"%(int(price)*((100-discount)/100)) + " "
            i += 1
        if dolar_sta_ind != None:
            price = sentence[dolar_sta_ind:n]
            if not price.isnumeric():
                    res += price
            else:
                res += f"%.2f"%(int(price)*((100-discount)/100))
        return res
            

