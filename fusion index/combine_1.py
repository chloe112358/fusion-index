import cv2
import numpy as np

# 讀圖
icc_image = cv2.imread('C:\\Users\\chloe\\Desktop\\ICC-20240205\\C2C12\\C3cell.jpg')
dapi_image = cv2.imread('C:\\Users\\chloe\\Desktop\\ICC-20240205\\C2C12\\C3.1new.jpg')

# 轉HSV
hsv = cv2.cvtColor(icc_image, cv2.COLOR_BGR2HSV)

# 取紅色
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])


mask = cv2.inRange(hsv, lower_red, upper_red)

# 紅色上的細胞核
dapi_masked = cv2.bitwise_and(dapi_image, dapi_image, mask=mask)


# 保存结果图像
cv2.imwrite('combine_1_1.jpg', dapi_masked)

# 顯示
cv2.imshow('DAPI with Red Overlay', dapi_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()