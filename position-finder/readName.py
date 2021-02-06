import numpy as np
import os



boardList = []
os.chdir("..\\test")
files = os.listdir()
print('BEFORE')
#print(files)

print(files[0])
temp = files[0].strip(".jpeg")
print("TEMP: " + temp)


for filename in files:
    filename = filename.strip(".jpeg")
    rows = filename.split("-")
    board = [["1" for i in range(8)] for j in range(8)]
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

    #print(board)  
    boardList.append(board)

#print(files)
print(boardList[-1])
print("SUCCESS!")