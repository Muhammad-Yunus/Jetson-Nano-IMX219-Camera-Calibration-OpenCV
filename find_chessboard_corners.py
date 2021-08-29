import numpy as np
import cv2
import os

# Parameter
CHESSBOARD_SIZE = (7,9)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CHESSBOARD_SIZE[0]*CHESSBOARD_SIZE[1],3), np.float32)
objp[:,:2] = np.mgrid[0:CHESSBOARD_SIZE[0],0:CHESSBOARD_SIZE[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.



for filename in os.listdir("capture/"):
	print("read filename %s" % filename)
	img = cv2.imread("capture/" + filename)
	if img is None :
		print("empty image with filename %s" % filename) 
		continue

	img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
	print(img.shape)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Find the chess board corners
	print("find chess corner for filename %s" % filename)
	ret, corners = cv2.findChessboardCorners(gray, CHESSBOARD_SIZE, None)

	# If found, add object points, image points (after refining them)
	if ret == True:
		print("chess corner found!")
		objpoints.append(objp)
		corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
		imgpoints.append(corners)

		# Draw and display the corners
		print("draw corner")
		cv2.drawChessboardCorners(img, CHESSBOARD_SIZE, corners2, ret)
		cv2.imshow('img', img)
		cv2.waitKey(0)

cv2.destroyAllWindows()

h,w = img.shape[:2]

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)

