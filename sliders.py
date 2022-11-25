import cv2
import numpy as np

img = cv2.imread('Battery Image.jpg', cv2.IMREAD_COLOR)

img = cv2.resize(img, (1000, 1000))

# cv2.imshow("Image2", img)

leftSide = img[150:200, 250:450]

rightSide = img[200:250, 650:850]

# cv2.imshow("Image", leftSide)
# cv2.imshow("Image3", rightSide)
cv2.waitKey(0)



def empty(i):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 0, 255, empty)

while True:

    imgHSV = cv2.cvtColor(leftSide, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(leftSide, leftSide, mask=mask)

    cv2.imshow("Mask Images", mask)
    cv2.imshow("Original Images", leftSide)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        break