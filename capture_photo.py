import cv2
import time
from gst_cam import camera

w, h = 3280, 2464
cap_0 = cv2.VideoCapture(camera(0, w, h))

time.sleep(3)

i = 0
while True :
	ret_0, frame_0 = cap_0.read()

	if not ret_0 :
		break

	cv2.imshow("frame 0", cv2.resize(frame_0, (0,0), fx=0.25, fy=0.25))
	
	key = cv2.waitKey(10)
	if key == ord("q"):
		break

	if key == ord("s"):
		print("saved image %d" % i)
		cv2.imwrite("capture/cam_0_%d.jpg" % i, frame_0)
		i += 1

	if i == 20 :
		break

cv2.destroyAllWindows()
cap_0.release()
