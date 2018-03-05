#!/usr/bin/python
import os.path
import os
import shutil
import re

# Create the videos directory in the current location
# If the directory exists ignore it
def createDirectory():
    directory = "videos"
    if not os.path.isdir("./" + directory + "/"):
        os.mkdir("./" + directory + "/")
        print("Videos Folder Created.")
    else:
        print("Video Folder Exists.")
        print("---------------------")

# Move all the files in the root directory with the .wmv extension
# to the videos folder
def moveVideos():
    for file in os.listdir("."):
        if os.path.splitext(file)[1] == ".wmv":
            print("Moving:", file)
            shutil.move(file, os.path.join("videos", file))
def createHTML():
    videoDirectory = os.listdir("videos")
    f = open("list.html", "w")
    f.write('<html><head></head><body>\n')
    f.write('\t<ul>\n')
    f.writelines(['\t\t<li><a href="videos/%s">%s</a></li>\n' % (fname, fname) for fname in videoDirectory])
    f.write('\t</ul>\n')
    f.write('</body></html>\n')

createDirectory()
moveVideos()
createHTML()
