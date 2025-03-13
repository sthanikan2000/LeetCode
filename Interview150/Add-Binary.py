class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output=\\
        carry=0
        a_=list(a)
        b_=list(b)
        while a_ or b_ or carry:
            sum_ = carry
            if a_:
                sum_+=int(a_.pop(-1))
            if b_:
                sum_+=int(b_.pop(-1))

            output = str(sum_%2) + output
            carry = sum_//2
        return output

        