import os
import cv2
import utils

# read video
video_foldername = os.getcwd +  '\Videos'
video_filename = 'IMG_3836.MOV'
video_path = os.path.join(video_foldername, video_filename)
vidcap = cv2.VideoCapture(video_path)

# check whether saved before
pwd = os.getcwd()
frame_foldername = os.path.join(pwd, 'Frames')
check = utils.check_if_saved_before(frame_foldername, video_filename)


