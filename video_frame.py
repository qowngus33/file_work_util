"""
Read Video and extract frames from it
"""
import cv2

vidcap = cv2.VideoCapture('/Volumes/NONAME/0807_test.mp4')
success, image = vidcap.read()
pathOut = '/Volumes/NONAME/0807_test/'

count = 0
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))    # added this line
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite(pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1
