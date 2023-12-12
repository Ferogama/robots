import cv2
import numpy as np

# Функция для вычисления фокусного расстояния камеры
def calculate_focal_length(actual_width, image_width, distance_to_object):
    focal_length = (distance_to_object * image_width) / actual_width
    return focal_length

# Функция для вычисления расстояния до объекта
def calculate_distance(actual_width, image_width, focal_length):
    distance = (actual_width * focal_length) / image_width
    return distance

image = cv2.imread("/Users/sidmeiers/Desktop/selfi.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_color = np.array([20, 100, 100])  # Нижний порог цвета в HSV для желтого объекта
upper_color = np.array([30, 255, 255])  # Верхний порог цвета в HSV для желтого объекта
mask = cv2.inRange(hsv, lower_color, upper_color)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Берем самый большой контур - наш объект
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    width_pixels = w
    actual_width = 15  # Фактическая ширина объекта в см
    distance_to_object = 50  # Расстояние до объекта в см

    # Вычисление фокусного расстояния камеры
    focal_length = calculate_focal_length(actual_width, width_pixels, distance_to_object)
    print(f"Приблизительное фокусное расстояние камеры: {focal_length} пикселей")

    # Вычисление расстояния до объекта
    computed_distance = calculate_distance(actual_width, width_pixels, focal_length)
    print(f"Вычисленное расстояние до объекта: {computed_distance} сантиметров")

    cv2.putText(image, f"Distance: {computed_distance:.2f} cm", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.namedWindow('Detected Object', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Detected Object', 400, 300)
    cv2.imshow('Detected Object', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Контуры не обнаружены")
