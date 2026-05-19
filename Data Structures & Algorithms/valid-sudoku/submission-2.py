class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for x in range(0, 9): #rows dup check
            dupCheck = []
            for y in range(0,9):
                if board[x][y] == '.':
                    continue
                if board[x][y] not in dupCheck:
                    dupCheck.append(board[x][y])
                else:
                    return False
        
        for x in range(0, 9): #cols dub check
            dupCheck = []
            for y in range(0, 9):
                if board[y][x] == '.':
                    continue
                if board[y][x] not in dupCheck:
                    dupCheck.append(board[y][x])
                else:
                    return False
        
        for x in range(0, 9, 3): #3x3 check
            for y in range(0, 9, 3):
                dupCheck = []
                for x2 in range(0, 3):
                    for y2 in range(0, 3):
                        if board[x + x2][y + y2] == '.':
                            continue 
                        if board[x + x2][y + y2] not in dupCheck:
                            dupCheck.append(board[x + x2][y + y2])
                        else:
                            return False

        return True


        