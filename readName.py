import numpy as np
name = "1B1B1K2-3p1N2-6k1-R7-5P2-4q3-7R-1B6"

rows = name.split("-")
print(rows)

board = [["1" for i in range(8)] for j in range(8)]
print(board)
rowNum = 0
for row in rows:
    colNum = 0
    for char in row:
        if(char.isdigit()):
            numBlank = ord(char) - 48 #48 = '0'
            
            for i in range(numBlank):
                board[rowNum][colNum] = "0"
                colNum += 1
        else:
            board[rowNum][colNum] = char
            colNum += 1 
    rowNum += 1

print(board)  


