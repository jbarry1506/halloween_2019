# before using, install ...
    # sudo apt-get install python-picamera
import picamera
import datetime
# import the sewerlib module
from sewerlib import sewercam
import os.path
from os.path import extenduser

# set home directory location
home = extenduser("~")

# set file location
fileLoc = home+'/Pictures/'

# set up the camera
camera = picamera.PiCamera()

# store the datetime for the video name
partyTime = datetime.datetime.now()

camTime = str(partyTime.year) + "_"\
    +str(partyTime.month) + "_"\
    +str(partyTime.day) + "_"\
    +str(partyTime.hour) + "_"\
    +str(partyTime.minute) + "_"\
    +str(partyTime.second)

floaterSeen = sewercam.it_saw_you()

# main
if __name__ == "__main__":
    sewercam.cam_controller(camera, floaterSeen, camTime, fileLoc)