class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # [\horizontal\,\vertical\,\grid\]
            check = {'1': [False, False, False], '2': [False, False, False], '3': [False, False, False], '4': [False, False, False], '5': [False, False, False], '6': [False, False, False], '7': [False, False, False], '8': [False, False, False], '9': [False, False, False]}
            for j in range(9):
                # check by row
                row_ele = board[i][j]
                if  row_ele != \.\:
                    if not check[row_ele][0]:
                        check[row_ele][0] = True
                    else:
                        return False

                # check by column
                col_ele = board[j][i]
                if  col_ele != \.\:
                    if not check[col_ele][1]:
                        check[col_ele][1] = True
                    else:
                        return False

                # Check by grid
                grid_ele = board[(i//3)*3+(j//3)][(i%3)*3+(j%3)]
                if  grid_ele != \.\:
                    if not check[grid_ele][2]:
                        check[grid_ele][2] = True
                    else:
                        return False
        return True




        