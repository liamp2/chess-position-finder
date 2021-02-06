import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("..\\test\\1b1B1Qr1-7p-6r1-2P5-4Rk2-1K6-4B3-8.jpeg", cv2.IMREAD_COLOR)

squares = []
y = 0
x = 0

for i in range(8):
    for j in range(8):
        square = img[y:y+50, x:x+50]
        squares.append(square)
        x += 50
    x = 0
    y += 50


#img2 = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)


#img = cv2.imread("bookpage.jpg", cv2.IMREAD_COLOR)
#retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#squareRegion = img[0:50, 50:100]
#img[250:300, 50:100] = [0, 0, 255]
#print(squareRegion)
#cv2.rectangle(img, (0,0), (50, 50), (255, 0, 0), -1) 

#font = cv2.FONT_HERSHEY_COMPLEX
#scv2.putText(img, 'Square', (200, 200), font, 0.5, (255, 255, 255))

cv2.imshow('image', img)
i = 0
for i in range(64):
    cv2.imshow("square" + str(i), squares[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
