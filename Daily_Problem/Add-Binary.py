class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output=\\
        carry = \0\
        min_len = min(len(a),len(b))
        for i in range(1,min_len+1):
            if carry == \0\:
                if a[-i] == b[-i] == \0\:
                    output = \0\ + output
                elif a[-i] == b[-i]:
                    output = \0\ + output
                    carry = \1\
                else:
                    output = \1\ + output
            elif a[-i] == b[-i] == \0\:
                output = \1\ + output
                carry = \0\
            elif a[-i] == b[-i]:
                output = \1\ + output
                carry = \1\
            else:
                output = \0\ + output
                carry = \1\
        if len(a) != len(b):
            if len(a) > len(b):
                x = a
            else:
                x = b
            for i in range(-min_len-1,-len(x)-1,-1):
                if x[i] == carry == \1\:
                    output = \0\ + output
                    carry = \1\
                elif x[i] == carry:
                    output = \0\ + output
                else:
                    output = \1\ + output
                    carry = \0\
            
        if carry == \1\:
            return \1\+output
        else:
            return output




        # carry=0
        # a_=list(a)
        # b_=list(b)
        # while a_ or b_ or carry:
        #     sum_ = carry
        #     if a_:
        #         sum_+=int(a_.pop(-1))
        #     if b_:
        #         sum_+=int(b_.pop(-1))

        #     output = str(sum_%2) + output
        #     carry = sum_//2
        # return output

        