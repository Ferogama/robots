from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("D:/git/robots/runs/segment/train/weights/best.pt")
# please edit the path to your model
# model = YOLO("yolov8m-seg.pt") #or try pretrained model
image = cv2.imread('C:/Users/fero/Desktop/data/train/images/tt.jpg')
results = model(image)
h, w, _ = image.shape
result = results[0]
if result.masks is not None:
    for i, mask in enumerate(result.masks.data):
        mask = mask.cpu().numpy().astype(np.uint8)
    mask = cv2.resize(mask, (w, h))
    contours, hierarchy = cv2.findContours(mask,
                                           cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
# image = result.plot()
cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()
