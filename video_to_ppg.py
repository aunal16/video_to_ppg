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
    limit = 60*10  # how many frames you want to use, uncomment line 44 to use
    frames = list()
    os.chdir(path)
    print(path)
    for filename in glob.iglob('*.jpg'):
        im = Image.open(filename)
        frames.append(np.array(im))
        im.close()
        if str(limit) in filename: break

height = np.size(frames[0], 0)
width  = np.size(frames[0], 1)
depth  = np.size(frames[0], 2)

reds   = list()
greens = list()
blues  = list()

for img in frames:
    red_sum   = 0
    green_sum = 0
    blue_sum  = 0
    for i in range(height):
        for j in range(width):
            red_sum   += img[i][j][0]
            green_sum += img[i][j][1]
            blue_sum  += img[i][j][2]
            
    reds.append  (red_sum)
    greens.append(green_sum)
    blues.append (blue_sum)

plt.figure(0)
plt.plot(range(len(reds)), reds)
plt.plot(range(len(greens)), greens)
plt.plot(range(len(blues)), blues)

plt.figure(1)
plt.plot(np.array(range(len(reds)))/(len(reds)-1), reds)

plt.show()
