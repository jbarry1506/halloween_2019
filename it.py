# before using, install ...
    # sudo apt-get install python-picamera
import picamera
import datetime
# import the sewerlib module
from sewerlib import sewercam
# import os
import os.path
from os.path import expanduser
import time


# set pi home directory location
home = expanduser("~")

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

if __name__ == "__main__":
    program_running = True
    floaterSeen = False
    avg = None
    lastUploaded = datetime.datetime.now()
    motionCounter = 0

    cam_init = sewercam.init_camera()
    camera.capture(fileLoc+camTime+".jpg")

    while floaterSeen == False:
        # check to see if the camera recognizes motion
        floaterSeen = sewercam.it_saw_you()
        time.sleep(2)

    # start the camera functions
    sewercam.cam_controller(camera, floaterSeen, camTime)

