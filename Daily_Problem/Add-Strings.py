class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        output = \\
        min_len = min(len(num1),len(num2))
        for i in range(1,min_len+1):
            x = int(num1[-i]) + int(num2[-i]) + carry
            if x>9:
                carry = 1
                output = str(x-10) + output
            else:
                carry = 0
                output = str(x) + output
        if len(num1) > len(num2):
            num = num1
        else:
            num = num2
        if carry:
            for i in range(-min_len-1,-len(num)-1,-1):
                x = int(num[i]) + carry
                if x>9:
                    carry = 1
                    output = str(x-10) + output
                else:
                    carry = 0
                    output = str(x) + output
        else:
            return num[-len(num):-min_len] + output
        if carry:
            return \1\ + output
        else:
            return output

        