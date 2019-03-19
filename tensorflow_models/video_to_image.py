import os
import cv2
import numpy as np
import sys

sys.path.append("..")
VIDEO_NAME = "GOPR9840.MP4"
cwd = os.getcwd()
PATH_TO_VIDEO = os.path.join(cwd,VIDEO_NAME)

vidcap = cv2.VideoCapture(PATH_TO_VIDEO)

count = 0
while(vidcap.isOpened()):  
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("drone_images/frame%d.jpg" % count, image) 
  count += 1
vidcap.release()