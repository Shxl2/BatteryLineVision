import cv2
import numpy


def detectdefect(img1, img2):
    for i in range(49, 0, -1):
        for j in range(200):
            if (img1[i][j] == 255 or img2[i][j]) and j < 75:
                print("Defective")
                return


img = cv2.imread('Battery Image.jpg', cv2.IMREAD_COLOR)

img = cv2.resize(img, (1000, 1000))

# cv2.imshow("Image2", img)

leftSide = img[150:200, 250:450]

rightSide = img[200:250, 650:850]

rightSide = cv2.inRange(rightSide, (0, 10, 168), (255, 153, 255))
leftSide = cv2.inRange(leftSide, (0, 10, 168), (255, 153, 255))
# cv2.imshow("Image", leftSide)
# cv2.imshow("Image3", rightSide)


cv2.waitKey(0)

detectdefect(leftSide, rightSide)
