class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # [\horizontal\,\vertical\,\grid\]
            check = [[False]*3 for i in range(9)]
            for j in range(9):
                # check by row
                row_ele = board[i][j]
                if  row_ele != \.\:
                    if not check[int(row_ele)-1][0]:
                        check[int(row_ele)-1][0] = True
                    else:
                        return False

                # check by column
                col_ele = board[j][i]
                if  col_ele != \.\:
                    if not check[int(col_ele)-1][1]:
                        check[int(col_ele)-1][1] = True
                    else:
                        return False

                # Check by grid
                grid_ele = board[(i//3)*3+(j//3)][(i%3)*3+(j%3)]
                if  grid_ele != \.\:
                    if not check[int(grid_ele)-1][2]:
                        check[int(grid_ele)-1][2] = True
                    else:
                        return False
        return True




        