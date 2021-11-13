
EMPTY = "*"
H = "H"
A = "A"
L = "L"
O = "O"
welcomeBoard = []

for i in range(5):
    row = [EMPTY for i in range(5)]
    welcomeBoard.append(row)
    column = [EMPTY for i in range(5)]
    welcomeBoard.append(column)
 
 
welcomeBoard[3][0] = H
welcomeBoard[3][1] = A
welcomeBoard[3][2] = L
welcomeBoard[3][3] = L
welcomeBoard[3][4] = O 

print(welcomeBoard)   