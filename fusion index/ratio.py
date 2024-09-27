import cv2
import numpy as np

#讀圖
image1 = cv2.imread('C:\\Users\\chloe\\Desktop\\ICC-20240205\\C2C12\\C3.1new.jpg')
image2 = cv2.imread('C:\\Users\\chloe\\Desktop\\cell_counting\\20240222\\combine_1.jpg')

#轉HSV
hsv_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
hsv_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

# 取藍色
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

blue_mask1 = cv2.inRange(hsv_image1, lower_blue, upper_blue)
blue_mask2 = cv2.inRange(hsv_image2, lower_blue, upper_blue)

# 算面積
blue_area1 = np.sum(blue_mask1 / 255)
blue_area2 = np.sum(blue_mask2 / 255)

print("全部藍色：", blue_area1)
print("部分：", blue_area2)
print("相除：", blue_area2/blue_area1)