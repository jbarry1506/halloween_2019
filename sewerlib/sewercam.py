
import time
import picamera
from os import path
from os.path import expanduser

# define function to control the camera
def cam_controller(cam, seen, dt):
    # home
    home = expanduser("~")
    fl = home+"/Pictures/"
    filetest = str(path.exists(home+'/Pictures'))
    print(filetest)
    
    if seen:
        cam.capture(fl+dt+".jpg")
        cam.start_recording(fl+dt+".h264")
        time.sleep(5)
        poll_cam = it_saw_you()
        if not poll_cam:
            cam.stop_recording()


def it_saw_you():
    scare = True
    return scare
