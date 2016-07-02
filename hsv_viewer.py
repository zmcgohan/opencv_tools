import cv2
import numpy as np

increment = 0
last_inc = 0
last_press_ticks = 0

hsv_range = 10
h = 90
s = v = 255

lower_range = np.array([ max(0,h-hsv_range), 0, 0 ], dtype=np.uint8)
upper_range = np.array([ min(180,h+hsv_range), 255, 255 ], dtype=np.uint8)

def trackbar_update(_):
	global hsv_range, h, s, v, lower_range, upper_range
	hsv_range = cv2.getTrackbarPos('Range', 'Results')
	h = cv2.getTrackbarPos('H', 'Results')
	s = cv2.getTrackbarPos('S', 'Results')
	v = cv2.getTrackbarPos('V', 'Results')
	print "+- {}, H: {}, S: {}, V: {}".format(hsv_range, h, s, v)
	lower_range[0] = max(0,h-hsv_range)
	upper_range[0] = min(180,h+hsv_range)
	draw_results()

def draw_results():
	global hsv_range, h, s, v, lower_range, upper_range
	mask = cv2.inRange(img_hsv, lower_range, upper_range)
	masked = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
	res = cv2.cvtColor(masked, cv2.COLOR_HSV2BGR)
	cv2.imshow('Results', res)

cv2.namedWindow('Results')
cv2.createTrackbar('Range', 'Results', hsv_range, 128, trackbar_update)
cv2.createTrackbar('H', 'Results', h, 180, trackbar_update)
cv2.createTrackbar('S', 'Results', s, 255, trackbar_update)
cv2.createTrackbar('V', 'Results', v, 255, trackbar_update)

img = cv2.imread('cube-couch.JPG')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

draw_results()

while 1:
	if increment > 0 and (cv2.getTickCount()-last_press_ticks) / cv2.getTickFrequency() > 1.0:
		increment = 0
	# set increment value
	inc = increment
	if inc == 0:
		inc = last_inc
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	elif ord('0') <= k <= ord('9'):
		increment *= 10
		increment += (9-(ord('9')-k))
		print "Inc: {}".format(increment)
		last_press_ticks = cv2.getTickCount()
	elif k == ord('h'):
		cv2.setTrackbarPos('H', 'Results', max(0,h-inc))
		last_inc = inc
	elif k == ord('H'):
		cv2.setTrackbarPos('H', 'Results', min(180,h+inc))
		last_inc = inc
	elif k == ord('s'):
		cv2.setTrackbarPos('S', 'Results', max(0,s-inc))
		last_inc = inc
	elif k == ord('S'):
		cv2.setTrackbarPos('S', 'Results', min(255,s+inc))
		last_inc = inc
	elif k == ord('v'):
		cv2.setTrackbarPos('V', 'Results', max(0,v-inc))
		last_inc = inc
	elif k == ord('V'):
		cv2.setTrackbarPos('V', 'Results', min(255,v+inc))
		last_inc = inc
	elif k == ord('r'):
		cv2.setTrackbarPos('Range', 'Results', max(0,hsv_range-inc))
		last_inc = inc
	elif k == ord('R'):
		cv2.setTrackbarPos('Range', 'Results', min(128,hsv_range+inc))
		last_inc = inc
	if k is not 255:
		trackbar_update(None)
		

cv2.destroyAllWindows()
