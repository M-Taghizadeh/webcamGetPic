import cv2
camera = cv2.VideoCapture(0)
retur_value, img = camera.read()
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('C:/Users/Zanis/Desktop/test.jpg', img)
