import cv2
import numpy as np
import sys

#if len(sys.argv) < 2:
#	print "Include an image to search."
#	sys.exit(0)

#img_src = sys.argv[1]

for i in dir(cv2):
	if "EVENT" in i:
		print i

def mouse_clicked(e, x, y, flags, param):
	print e.name
	if e == cv2.EVENT_LBUTTONUP:
		print "Left clicked"

img_src = "/Users/zmcgohan/projects/rubiks-cube-app/images/three-sides-1.jpg"
img = cv2.imread(img_src)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_equalized = cv2.equalizeHist(img)
res = np.hstack(( img, img_equalized ))
cv2.imshow('Image', res)
cv2.waitKey(0)
print img

cv2.namedWindow("Hue Selection")
cv2.setMouseCallback("Hue Selection", mouse_clicked)

while 1:
	cv2.imshow("Hue Selection", img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		sys.exit(0)

cv2.destroyAllWindows()
