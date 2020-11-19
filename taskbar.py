import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('Test_Images\Test1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('ls','image',0,255,nothing)
cv2.createTrackbar('lv','image',0,255,nothing)
cv2.createTrackbar('hh','image',0,255,nothing)
cv2.createTrackbar('hs','image',0,255,nothing)
cv2.createTrackbar('hv','image',0,255,nothing)


while(1):
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('lh','image')
    g = cv2.getTrackbarPos('ls','image')
    b = cv2.getTrackbarPos('lv','image')
    rr = cv2.getTrackbarPos('hh','image')
    gg = cv2.getTrackbarPos('hs','image')
    bb = cv2.getTrackbarPos('hv','image')
#     s = cv2.getTrackbarPos(switch,'image')
    
    lower_hsv = np.array([r, g, b])
    higher_hsv = np.array([rr, gg, bb])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    cv2.imshow('image',mask)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
