import os
import cv2
import utils

# read video
cwd = os.getcwd()
video_folder_dir = os.path.join(cwd, 'Videos')
video_file_name  = 'IMG_3836.MOV'

video_dir = os.path.join(video_folder_dir, video_file_name)
vidcap = cv2.VideoCapture(video_dir)

# check whether saved before
frame_folder_dir = os.path.join(cwd, 'Frames')
check = utils.check_if_saved_before(frame_folder_dir, video_file_name)


