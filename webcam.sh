#!/bin/bash
# get time stamp filename
camname=~/webcam/pics/$(date +"%Y-%m-%d-%H-%M-%S").jpg
echo $camname

# fswebcam -p YUYV is for logitech C170 
sudo fswebcam -r 640x480 -p YUYV -S 60  $camname

# send this to remote image
scp $camname rmqlife@www.rmqlife.com:~/pics/cam.jpg
# rsync $camname rmqlife@www.rmqlife.com:~/pics/cam.jpg

