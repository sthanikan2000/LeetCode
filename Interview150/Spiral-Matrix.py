class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t_l = [0,0]
        t_r = [0,len(matrix[0])-1]
        b_l = [len(matrix)-1,0]
        b_r = [len(matrix)-1,len(matrix[0])-1]
        i = [0,0]
        res = []
        current = \l-r\
        for _ in range(len(matrix)*len(matrix[0])):
            res.append(matrix[i[0]][i[1]])
            if current == \l-r\:
                if i[1]<t_r[1]:
                    i[1]+=1
                else: # i[1]==t_r[1]
                    i[0] += 1
                    current = \t-b\
                    t_l[0] += 1
                    t_r[0] += 1
            elif current == \t-b\:
                if i[0]<b_r[0]:
                    i[0]+=1 
                else:
                    i[1] -= 1
                    current = \r-l\
                    t_r[1] -= 1
                    b_r[1] -= 1
            elif current == \r-l\:
                if i[1] > b_l[1]:
                    i[1] -= 1
                else:
                    i[0] -= 1
                    current = \b-t\
                    b_l[0] -= 1
                    b_r[0] -= 1
            else:
                if i[0] > t_l[0]:
                    i[0] -= 1
                else:
                    i[1] += 1
                    current = \l-r\
                    t_l[1] += 1
                    b_l[1] += 1
        return res





        