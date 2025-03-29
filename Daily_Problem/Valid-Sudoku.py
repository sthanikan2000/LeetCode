class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # [\horizontal\,\vertical\,\grid\]
            check = {'1': [False, False, False], '2': [False, False, False], '3': [False, False, False], '4': [False, False, False], '5': [False, False, False], '6': [False, False, False], '7': [False, False, False], '8': [False, False, False], '9': [False, False, False]}
            for j in range(9):
                # check by row
                if board[i][j] != \.\:
                    if not check[board[i][j]][0]:
                        check[board[i][j]][0] = True
                    else:
                        return False
                # check by column
                if board[j][i] != \.\:
                    if not check[board[j][i]][1]:
                        check[board[j][i]][1] = True
                    else:
                        return False
                # Check by grid
                if board[(i//3)*3+(j//3)][(i%3)*3+(j%3)] != \.\:
                    if not check[board[(i//3)*3+(j//3)][(i%3)*3+(j%3)]][2]:
                        check[board[(i//3)*3+(j//3)][(i%3)*3+(j%3)]][2] = True
                    else:
                        return False
        return True




        