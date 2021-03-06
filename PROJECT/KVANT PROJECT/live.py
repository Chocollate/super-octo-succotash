# This script will detect faces via your webcam.
# Tested with OpenCV3
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
count = len(os.listdir("photo"))
# Create the haar cascadeй
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	#print("Found {0} faces!".format(len(faces)))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



	# Display the resulting frame
	cv2.imshow('frame', frame)

	key = chr(cv2.waitKey(20) & 0xff)
	if key == 'q':
		break
	elif key == ' ':
		cv2.imwrite(
			"photo/image-" + str(count) + ".jpg",
			frame)
		count = count + 1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
