# USAGE OF STACK
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         mapping = {\I\:1, \V\:5, \X\:10, \L\:50, \C\:100, \D\:500, \M\:1000 }
#         result = 0
#         stack = []
#         for i in range(0,len(s)-1):
#             if not stack and mapping[s[i]]>=mapping[s[i+1]]:
#                 result += mapping[s[i]]
#             elif stack and mapping[s[i]]>=mapping[s[i+1]]:
#                 temp = mapping[s[i]]
#                 while stack:
#                     temp -= mapping[stack.pop(-1)]
#                 result += temp
#             # elif not stack and mapping[s[i]]<mapping[s[i+1]]:
#             #     stack.append(s[i])
#             else:
#                 stack.append(s[i])
#         # print(result,stack,i)
#         if stack:
#             temp = mapping[s[len(s)-1]]
#             while stack:
#                 temp -= mapping[stack.pop(-1)]
#             result += temp
#         else:
#             result += mapping[s[len(s)-1]]
#         return result

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {\I\:1, \V\:5, \X\:10, \L\:50, \C\:100, \D\:500, \M\:1000}
        total = values[s[0]]
        pre = s[0]
        for i in s[1:]:
            if values[pre] >= values[i]:
                total += values[i]
                pre = i
            else:
                total += values[i] - 2*values[pre]
                pre = i
        return total
           
        