import cv2
import numpy as np

image_path = "C:/Users/fero/Desktop/krestiki/4.jpg"
def find_cell_centers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cell_centers = []
    for contour in contours:
        # Вычисление координат центра контура
        M = cv2.moments(contour)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            cell_centers.append((center_x, center_y))
    if len(cell_centers) != 9:
        raise ValueError("Не удалось найти ровно 9 клеток на изображении")
    cell_centers = np.array(cell_centers).reshape(3, 3, 2)

    return cell_centers
image = cv2.imread(image_path)
copy_image = image.copy()
centers = find_cell_centers(image)
for row in centers:
    for center in row:
        cv2.circle(copy_image, tuple(center), 5, (0, 255, 0), -1)
centers = find_cell_centers(image)
print("Координаты центров клеток:")
print(centers)
cv2.imshow('Marked Image', copy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
