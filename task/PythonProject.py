import cv2
import numpy as np

def recognize_tic_tac_toe(image_path):
    
    image = cv2.imread(image_path)

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    result_array = []

    # Проход по контурам
    for contour in contours:
        # Получение прямоугольника, ограничивающего контур
        x, y, w, h = cv2.boundingRect(contour)
        cell_width = w // 3
        cell_height = h // 3

        # Проход по частям клетки
        for i in range(3):
            for j in range(3):
                
                roi_x = x + j * cell_width + cell_width // 3
                roi_y = y + i * cell_height + cell_height // 3
                roi_w = cell_width // 3
                roi_h = cell_height // 3

                # Получение области интереса (ROI) внутри клетки
                roi = image[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

                # Детекция кругов (символ 'O')
                circles = cv2.HoughCircles(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY), cv2.HOUGH_GRADIENT, dp=1,
                                           minDist=20, param1=50, param2=30, minRadius=10, maxRadius=30)

                # Если обнаружены круги, то это 'O'
                if circles is not None:
                    symbol = 'O'
                else:
                    # Если круги не обнаружены, проверяем темные пиксели
                    if np.any(roi < 128):
                        symbol = 'X'
                    else:
                        # Если нет темных пикселей, то клетка пустая
                        symbol = '-'

            
                result_array.append(symbol)

                cv2.rectangle(image, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (0, 255, 0), 2)
                cv2.putText(image, symbol, (roi_x + 10, roi_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2,
                            cv2.LINE_AA)

    
    cv2.imshow("Visualization", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    if len(result_array) == 9:
        return result_array
    else:
        return None 


image_path = 'C://Users//Papa//Downloads//gg.png'
result = recognize_tic_tac_toe(image_path)
print(result)
