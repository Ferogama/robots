import cv2
#для отображения графиков и изображений
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/fero/Desktop/12/3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

counters, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, counters, -1, (0,255,0), 2)
plt.imshow(image)
plt.show()