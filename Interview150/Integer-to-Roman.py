class Solution:
    def intToRoman(self, num: int) -> str:
        maps = [(1000,\M\), (500,\D\), (100,\C\), (50,\L\), (10,\X\), (5,\V\), (1,\I\)]
        result = \\
        stack=\\
        for i in range(len(maps)):                
            # print(result,num, i)
            result += maps[i][1]*(num//maps[i][0])
            num %= maps[i][0]

            num_str=str(num)
            if num_str[0] not in [\4\,\9\]:
                continue

            if i%2==0 and num >= maps[i][0]-maps[i+2][0]:
                result += (maps[i+2][1]+maps[i][1])
                num -= (maps[i][0]-maps[i+2][0])

            elif num >= maps[i][0]-maps[i+1][0]:
                result += (maps[i+1][1]+maps[i][1])
                num -= (maps[i][0]-maps[i+1][0])

        return result

                



