
import time
import datetime
from os import path
from os.path import expanduser
import json
import argparse

# need install with pip
import picamera

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
	help="path to the JSON configuration file")
args = vars(ap.parse_args())


def init_camera():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = tuple(conf["resolution"])
    camera.framerate = conf["fps"]
    rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))
    
    # allow the camera to warmup, then initialize the average frame, last
    # uploaded timestamp, and frame motion counter
    time.sleep(conf["camera_warmup_time"])
    initialization = "[INFO] warming up..."
    return initialization


# define function to control the camera
def cam_controller(cam, seen, dt):
    # home
    home = expanduser("~")
    fl = home+"/Pictures/"
    filetest = str(path.exists(home+'/Pictures'))
    print(filetest)

    if seen:
        cam.start_recording(fl+dt+".h264")
        time.sleep(5)
        poll_cam = True
        while poll_cam:
            poll_cam = it_saw_you()
            
        cam.stop_recording()


def it_saw_you():
    scare = True
    return scare
