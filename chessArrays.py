EMPTY = "-"
ROOK = "ROOK"
PAWN = "PAWN"
KNIGHT = "KNIGHT"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][0] = PAWN

print(board)    