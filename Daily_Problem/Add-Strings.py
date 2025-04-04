class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        output = \\
        min_len = min(len(num1),len(num2))
        for i in range(1,min_len+1):
            x = int(num1[-i]) + int(num2[-i]) + carry
            carry = x // 10
            output = str(x%10) + output
        if len(num1) > len(num2):
            num = num1
        else:
            num = num2
        for i in range(-min_len-1,-len(num)-1,-1):
            x = int(num[i]) + carry
            carry = x // 10
            output = str(x%10) + output
        if carry:
            return \1\ + output
        else:
            return output

        