import os
import cv2
import utils
import glob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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
else:
    # if frames already exist
    frames = list()
    os.chdir(path)
    print(path)
    for filename in glob.iglob('*.jpg'):
        img = Image.open(filename)
        frames.append(np.array(img))
        img.close()
        if "35" in filename: break

plt.imshow(frames[0])
plt.show()
