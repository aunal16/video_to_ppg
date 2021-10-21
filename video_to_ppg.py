import os
import cv2
import utils

# read video
cwd = os.getcwd()
video_folder_dir = os.path.join(cwd, 'Videos')
video_file_name  = 'IMG_3836.MOV'

video_dir = os.path.join(video_folder_dir, video_file_name)

# check whether saved before. if not, create the file
frame_folder_dir = os.path.join(cwd, 'Frames')
path, check = utils.check_if_saved_before(frame_folder_dir, video_file_name)

if not check:
    # if video is not splitted into frames before
    frames = list()
    vidcap = cv2.VideoCapture(video_dir)
    # get first frame
    success,image = vidcap.read()

    count = 0
    while success:
        frames.append(image)
        os.chdir(path)
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1




