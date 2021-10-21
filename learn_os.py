import os

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

foldername = "Frames"
newdir = os.path.join(cwd, foldername)
print(newdir)
