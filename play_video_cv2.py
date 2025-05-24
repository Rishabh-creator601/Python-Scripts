import cv2 ,os 

def play_video(path,play_gray=False,wait_time=25):

	""" wait_time should be 25 prefeered for video"""

	capture = cv2.VideoCapture(path)

	while capture.isOpened() ==True:

		ret,frame = capture.read()

		if ret is True:


			if play_gray == False:

				title =  "Video Playing By Ryuga"


				cv2.namedWindow(title,cv2.WINDOW_AUTOSIZE)

				cv2.resizeWindow(title,1280,720)
				
				cv2.imshow(title,frame)

			else:
				frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				cv2.imshow("Gray Frame Playing By Ryuga",frame)


			if cv2.waitKey(wait_time) & 0xFF == ord("q"):
				break 
		else:
			break


	capture.release()
	cv2.destroyAllWindows() 





